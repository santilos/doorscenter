# coding=utf8
import os, io, tarfile, cStringIO, ftplib, urllib, urllib2, datetime, random, threading, Queue

class Uploader(threading.Thread):
    '''Загрузка на FTP в потоке'''
    
    def __init__(self, queue, host, login, password, remotePath, fileName, fileObj, makeInit):
        '''Инициализация'''
        threading.Thread.__init__(self)
        self.queue = queue
        self.host = host
        self.login = login
        self.password = password
        self.remotePath = remotePath
        self.fileName = fileName
        self.fileObj = fileObj
        self.makeInit = makeInit

    def run(self):
        self.queue.get()
        try:
            ftp = ftplib.FTP(self.host, self.login, self.password)
            '''Пытаемся создать папку и установить нужные права'''
            if self.makeInit:
                try:
                    ftp.mkd(self.remotePath)
                except Exception as error:
                    pass
                try:
                    ftp.sendcmd('SITE CHMOD 02775 ' + self.remotePath)
                except Exception as error:
                    pass
            '''Отправляем файл'''
            try:
                ftp.storbinary('STOR ' + self.remotePath + '/' + self.fileName, self.fileObj)
            except Exception as error:
                print(error)
            try:
                ftp.quit()
            except Exception as error:
                print(error)
        except Exception as error:
            print(error)
        self.queue.task_done()

class Doorway(object):
    '''Дорвей'''
    
    def __init__(self, url, title, chunks = 10):
        '''Инициализация'''
        self.url = url
        self.title = title
        self.chunks = chunks
        '''Создаем файлы в памяти'''
        self.tarFilesObjects = []
        self.tarFiles = []
        self.closed = False
        for n in range(self.chunks):
            self.tarFilesObjects.append(io.BytesIO())
            self.tarFiles.append(tarfile.open('', 'w:gz', fileobj=self.tarFilesObjects[n]))
        self.cmdFileObject = io.BytesIO()
        self.cmdFileObject.write('''<?php \n umask(0); \n symlink('/var/www/common/images', 'images'); \n symlink('/var/www/common/js', 'js'); \n ''')
        for n in range(self.chunks):
            self.cmdFileObject.write('''system('tar -zxf bean%d.tgz'); \n unlink('bean%d.tgz'); \n ''' % (n, n))
        self.cmdFileObject.write('''?>''')
        '''Задаем содержимое служебных файлов'''
        self.htaccessContents = '''RemoveHandler .html
AddType application/x-httpd-php .php .html'''
        self.robotsContents = '''User-agent: *
Allow: /
Disallow: /js/
Disallow: /*/js/'''
    
    def _Close(self):
        '''Закрываем архив'''
        if not self.closed:
            for n in range(self.chunks):
                self.tarFiles[n].close()
        self.closed = True
    
    def InitTemplate(self, templatePath):
        '''Добавляем к дорвею содержимое папки шаблона'''
        excludeList = ['.htaccess', 'dp_sitemap.html', 'index.html', 'robots.txt']
        if not self.closed:
            for fileName in os.listdir(templatePath):
                if fileName not in excludeList:
                    self.tarFiles[0].add(os.path.join(templatePath, fileName), arcname=fileName)
        '''Добавляем стандартные файлы'''
        self.AddPage('.htaccess', self.htaccessContents)
        self.AddPage('robots.txt', self.robotsContents)
    
    def AddPage(self, fileName, fileContents):
        '''Добавляем страницу к дорвею'''
        if not self.closed:
            fileContents = fileContents.encode('utf-8', 'ignore')
            fileBuffer = cStringIO.StringIO(fileContents)
            fileBuffer.seek(0)
            tarInfo = tarfile.TarInfo(name=fileName)
            tarInfo.size = len(fileContents)
            n = random.randint(0, self.chunks - 1)
            self.tarFiles[n].addfile(tarinfo=tarInfo, fileobj=fileBuffer)
            fileBuffer.close()
    
    def SaveToFile(self, fileName):
        '''Сохраняем дорвей в виде архива'''
        self._Close()
        for n in range(self.chunks):
            self.tarFilesObjects[n].seek(0)
            with open(fileName.replace('.tgz', '%d.tgz' % n), 'wb') as fd:
                fd.write(self.tarFilesObjects[n].read())
    
    def SaveToFolder(self, folderName):
        '''Сохраняем дорвей в папку'''
        self._Close()
        for n in range(self.chunks):
            self.tarFilesObjects[n].seek(0)
            tarfile.open('', 'r', fileobj=self.tarFilesObjects[n]).extractall(folderName)
    
    def UploadToFTP(self, host, login, password, remotePath):
        '''Загружаем архив с дорвеем на FTP и распаковываем там'''
        dateTimeStart = datetime.datetime.now()
        self._Close()
        queue = Queue.Queue()
        '''Загружаем командный файл'''
        queue.put('')
        self.cmdFileObject.seek(0)
        Uploader(queue, host, login, password, remotePath, 'cmd.php', self.cmdFileObject, True).start()
        queue.join()
        '''Загружаем части дора'''
        for n in range(self.chunks):
            queue.put('')
            self.tarFilesObjects[n].seek(0)
            Uploader(queue, host, login, password, remotePath, 'bean%d.tgz' % n, self.tarFilesObjects[n], False).start()
        queue.join()
        '''Дергаем командный урл'''
        try:
            urllib.urlopen(self.url + '/cmd.php')
        except Exception as error:
            print(error)
        print('Uploaded in %d sec.' % (datetime.datetime.now() - dateTimeStart).seconds)

    def GooglePing(self):
        '''Пинг гугла'''
        try:
            pingXml = '''<?xml version="1.0"?>
<methodCall>
    <methodName>weblogUpdates.ping</methodName>
    <params>
        <param>
            <value>%s</value>
        </param>
        <param>
            <value>%s</value>
        </param>
    </params>
</methodCall>''' % (self.title, self.url)
            request = urllib2.Request('http://blogsearch.google.com/ping/RPC2')
            request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
            response = urllib2.urlopen(request, pingXml).read()
            print('Ping %s.' % ('ok' if response.find('Thanks for the ping') > 0 else 'ERROR'))
        except Exception as error:
            print(error)
