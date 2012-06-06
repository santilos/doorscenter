# coding=utf8
import os, sys, argparse, threading, Queue, time
import pinterest, amazon, common

if __name__ == '__main__':
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

class PinterestBoard(object):  # workaround for unpickling
    pass

class LauncherSingle(object):
    '''Запускаем бота - одна команда'''
    
    def __init__(self, printPrefix=None):
        '''Инициализация'''
        self.bot = pinterest.PinterestBot(printPrefix)
        self.amazon = amazon.Amazon(printPrefix)
        self.loggedIn = False
    
    def Parse(self, command):
        '''Парсим команду'''
        parser = argparse.ArgumentParser(description='Private Pinterest Bot (c) search 2012', formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('--user', required=True, help='login or email; you must specify logins (or emails), passwords and proxy (if needed) in "users.txt"')
        parser.add_argument('--action', required=True, choices=['follow-users', 'unfollow-users', 'follow-boards', 'like-pins', 'repost-pins', 'comment-pins', 'post-amazon', 'userinfo'], help='action to execute')
        parser.add_argument('--countmin', default=1, type=int, help='minimal actions count to execute')
        parser.add_argument('--countmax', default=1, type=int, help='maximum actions count to execute')
        parser.add_argument('--keywords', default='', help='comma-separated keywords for scraping people, boards and pins; see also "--category"')
        parser.add_argument('--category', default='', help='you may specify a category for scraping instead of keywords; use "popular" for scraping popular pins')
        parser.add_argument('--boards', default='', help='comma-separated board names for repinning and posting new pins; you may specify a category after the colon sign')
        parser.add_argument('--department', default='All', help='amazon department for searching for goods')
        parser.add_argument('--batchfile', default='', help='commands file name for batch mode')  # аргумент нужен только для справки, реально используется только в LauncherBatch
        parser.add_argument('--threads', type=int, default=5, help='threads count for batch mode')  # аргумент нужен только для справки, реально используется только в LauncherBatch
        parser.add_argument('--testmode', action='store_true', help='test (or demo) mode, executes all available commands')  # аргумент нужен только для справки, реально используется только в LauncherTest
        parser.epilog = 'Pinterest categories list: %s.\n\nAmazon departments list: %s.' % (', '.join(self.bot.boardCategoriesList), ', '.join(self.amazon.departmentsList))
        
        args = parser.parse_args(command.split(' '))
        self.userLogin = args.user
        self.action = args.action
        self.actionsCountMin = args.countmin
        self.actionsCountMax = args.countmax
        self.keywordsList = args.keywords.split(',')
        self.category = args.category
        self.boardsList = args.boards.split(',')
        self.amazonDepartment = args.department
    
    def Execute(self, command):
        '''Выполняем команду'''
        if command != 'parsed':
            self.Parse(command)
        try:
            '''Логинимся'''
            if self.bot.user.login != self.userLogin:
                self.loggedIn = False
            if not self.loggedIn:
                if self.bot.Login(self.userLogin):
                    self.loggedIn = True
                else:
                    raise Exception('Cannot log in with user "%s"' % self.userLogin)
            
            '''Выполняем команду'''
            if self.action == 'follow-users':
                self.bot.FollowUsers(self.keywordsList, self.category, self.actionsCountMin, self.actionsCountMax)
            elif self.action == 'unfollow-users':
                self.bot.UnfollowUsers(self.actionsCountMin, self.actionsCountMax)
            elif self.action == 'follow-boards':
                self.bot.FollowBoards(self.keywordsList, self.category, self.actionsCountMin, self.actionsCountMax)
            elif self.action == 'like-pins':
                self.bot.LikePins(self.keywordsList, self.category, self.actionsCountMin, self.actionsCountMax)
            elif self.action == 'repost-pins':
                self.bot.RepostPins(self.keywordsList, self.category, self.actionsCountMin, self.actionsCountMax, self.boardsList)
            elif self.action == 'comment-pins':
                self.bot.CommentPins(self.keywordsList, self.category, self.actionsCountMin, self.actionsCountMax)
            elif self.action == 'post-amazon':
                self.bot.PostFromAmazon(self.keywordsList, self.actionsCountMin, self.actionsCountMax, self.boardsList, self.amazonDepartment)
            elif self.action == 'userinfo':
                self.bot.ShowUserInfo()
            else:
                raise Exception('Unknown action')
        except Exception as error:
            self.bot._Print('### Error running a command: %s' % error)


class LauncherSingleThread(threading.Thread):
    '''Запускаем бота - одна команда в потоке'''
    
    def __init__(self, batch, threadNumber):
        '''Инициализация'''
        threading.Thread.__init__(self)
        self.daemon = True
        self.batch = batch
        self.threadNumber = threadNumber
        self.printPrefix = 'Thread #%d - ' % self.threadNumber + (' ' * ((self.threadNumber - 1) * 4))
        self.launcher = LauncherSingle(self.printPrefix)
        self._ClearLoginAndProxy()
    
    def _ClearLoginAndProxy(self):
        '''Очищаем юзера и прокси'''
        self.launcher.userLogin = ''
        self.launcher.proxyHost = ''
    
    def RunningUserOrProxy(self, userLogin, proxyHost):
        '''Проверяем, выполняется ли команда с этим юзером или прокси'''
        return (self.launcher.userLogin == userLogin) or (self.launcher.proxyHost == proxyHost)
    
    def run(self):
        '''Главный метод'''
        common.PrintThreaded(self.printPrefix + 'Thread started')
        while not self.batch.commandsQueue.empty():
            command = self.batch.commandsQueue.get()
            self.launcher.Parse(command)
            if self.batch.ExecutionAllowed(self, self.launcher.userLogin, self.launcher.proxyHost):
                self.launcher.Execute('parsed')
                self._ClearLoginAndProxy()
            else:
                self.batch.commandsQueue.put(command)
            self.batch.commandsQueue.task_done()
        common.PrintThreaded(self.printPrefix + 'Thread finished')


class LauncherBatch(object):
    '''Запускаем бота - команды по списку'''
    
    def __init__(self):
        '''Инициализация'''
        self.commandsQueue = None
        self.threadsList = []
    
    def Parse(self, command):
        '''Парсим команду'''
        parser = argparse.ArgumentParser(description='Private Pinterest Bot (c) search 2012', formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('--batchfile', required=True, help='commands file name for batch mode')
        parser.add_argument('--threads', type=int, default=5, help='threads count for batch mode')
        
        args = parser.parse_args(command.split(' '))
        self.batchFileName = args.batchfile
        self.threadsCount = args.threads
        
        self.commandsList = []
        if os.path.exists(self.batchFileName):
            self.commandsList = open(self.batchFileName).read().splitlines()
            self.commandsList = [item.strip() for item in self.commandsList if (item.strip() != '') and not item.strip().startswith('#')]
            self.threadsCount = min(self.threadsCount, len(self.commandsList))
        else:
            print('### Error parsing batch file: File "%s" not found' % self.batchFileName)
    
    def Execute(self, command):
        '''Выполняем команды'''
        if command != 'parsed':
            self.Parse(command)
        if len(self.commandsList) == 0:
            return
        print('=== Executing commands from "%s" ...' % self.batchFileName)
        self.commandsQueue = Queue.Queue()
        for command in self.commandsList:
            self.commandsQueue.put(command)
        self.threadsList = []
        for n in range(self.threadsCount):
            thread = LauncherSingleThread(self, n + 1)
            self.threadsList.append(thread)
            thread.start()
        self.commandsQueue.join()
        print('=== Done commands from "%s"' % self.batchFileName)
    
    def ExecutionAllowed(self, callingThread, userLogin, proxyHost):
        '''Проверяем, выполняются ли команды с этим юзером или прокси'''
        for thread in self.threadsList:
            if thread != callingThread:
                if thread.RunningUserOrProxy(userLogin, proxyHost):
                    return False
        return True


#TODO: генератор заданий

class LauncherTest(object):
    '''Запускаем тест'''
    
    def __init__(self):
        '''Инициализация'''
        pass
    
    def Parse(self, command):
        '''Парсим команду'''
        parser = argparse.ArgumentParser(description='Private Pinterest Bot (c) search 2012', formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('--user', required=True, help='user\'s login or email')
        parser.add_argument('--keywords', required=True, help='keywords for testing')
        parser.add_argument('--category', required=True, help='category for testing')
        parser.add_argument('--boards', required=True, help='boards for testing')
        parser.add_argument('--testmode', required=True, action='store_true', help='test (or demo) mode, executes all available commands')
        
        args = parser.parse_args(command.split(' '))
        self.userLogin = args.user
        self.keywords = args.keywords
        self.category = args.category
        self.boards = args.boards
        
        self.commands =  '''
            --user=%LOGIN% --action=follow-users --countmin=1 --countmax=1 --keywords=%KEYWORDS%
            --user=%LOGIN% --action=follow-users --countmin=1 --countmax=1 --category=%CATEGORY%
            --user=%LOGIN% --action=unfollow-users --countmin=1 --countmax=1
            --user=%LOGIN% --action=follow-boards --countmin=1 --countmax=1 --keywords=%KEYWORDS%
            --user=%LOGIN% --action=follow-boards --countmin=1 --countmax=1 --category=%CATEGORY%
            --user=%LOGIN% --action=like-pins --countmin=1 --countmax=1 --keywords=%KEYWORDS%
            --user=%LOGIN% --action=like-pins --countmin=1 --countmax=1 --category=%CATEGORY%
            --user=%LOGIN% --action=repost-pins --countmin=1 --countmax=1 --keywords=%KEYWORDS% --boards=%BOARDS%
            --user=%LOGIN% --action=repost-pins --countmin=1 --countmax=1 --category=%CATEGORY% --boards=%BOARDS%
            --user=%LOGIN% --action=comment-pins --countmin=1 --countmax=1 --keywords=%KEYWORDS%
            --user=%LOGIN% --action=comment-pins --countmin=1 --countmax=1 --category=%CATEGORY%
            --user=%LOGIN% --action=post-amazon --countmin=1 --countmax=1 --keywords=%KEYWORDS% --boards=%BOARDS%
            --user=%LOGIN% --action=userinfo
        '''
        self.commands = self.commands.replace('%LOGIN%', self.userLogin)
        self.commands = self.commands.replace('%KEYWORDS%', self.keywords)
        self.commands = self.commands.replace('%CATEGORY%', self.category)
        self.commands = self.commands.replace('%BOARDS%', self.boards)
        self.commandsList = self.commands.splitlines()
        self.commandsList = [item.strip() for item in self.commandsList if (item.strip() != '') and not item.strip().startswith('#')]
    
    def Execute(self, command):
        '''Выполняем команды'''
        if command != 'parsed':
            self.Parse(command)
        if len(self.commandsList) == 0:
            return
        print('=== Running test mode ...')
        launcher = LauncherSingle()
        for command in self.commandsList:
            launcher.Execute(command)
        print('=== Done test mode')


def Dispatcher(command=None):
    '''Точка входа'''
    if not command:
        command = ' '.join(sys.argv[1:])
    if command.find('--batchfile') >= 0:
        launcher = LauncherBatch()
    elif command.find('--testmode') >= 0:
        launcher = LauncherTest()
    else:
        launcher = LauncherSingle()
    launcher.Execute(command)
    sys.exit()  # для упрощения разработки и отладки - предотвращаем повторный запуск


if __name__ == '__main__':
    if not common.DevelopmentMode():
        Dispatcher()
    command = '--user=searchxxx --keywords=shoes --category=design --boards=Home --testmode'
    command = '--user=searchxxx --keywords=shoes --category=design --boards="For the Home,My Home" --testmode'
    Dispatcher(command)