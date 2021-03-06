# coding=utf8
import os, shutil, urllib, ftplib, io, tarfile, datetime, agent, common, tplgen
from doorgen.doorgen import Doorgen

class DoorgenMineAgent(agent.BaseAgent):
    ''' Параметры (см. методы GetTaskDetails и SetTaskDetails):
    Входные: keywordsList, keywordsListAdd, templateFolder, domain, domainSub, domainFolder, 
    netLinksList, tdsId, documentRoot, ftpHost, ftpLogin, ftpPassword, ftpPort.
    Выходные: doorLinksList.
    
    Параметр domainFolder всегда должен начинаться на прямой слэш.
    
    Минимальное содержимое командного файла cmd.php (для загрузки по FTP в архиве):
    <?php system('tar -zxf bean.tgz'); unlink('bean.tgz'); ?>     
'''
    
    def _Settings(self):
        '''Настройки'''
        self.appTemplatesFolder = os.path.dirname(os.path.abspath(__file__)) + '/doorgen/templates'  # папка с шаблонами 
        self.appTextsFolder = os.path.dirname(os.path.abspath(__file__)) + '/doorgen/templates/texts'  # папка с текстовыми файлами
        self.appSnippetsFolder = os.path.dirname(os.path.abspath(__file__)) + '/snippets'  # папка со сниппетами
        if self.currentTask['domainSub'] == '':
            self.doorwayUrl = 'http://%s%s' % (self.currentTask['domain'], self.currentTask['domainFolder'])
        else:
            self.doorwayUrl = 'http://%s.%s%s' % (self.currentTask['domainSub'], self.currentTask['domain'], self.currentTask['domainFolder'])
        if self.doorwayUrl.endswith('/'):
            self.doorwayUrl = self.doorwayUrl[0:-1]
        if self.currentTask['domainSub'] == '':
            self.remoteFolder = '%s%s' % (self.currentTask['documentRoot'], self.currentTask['domainFolder'])
        else:
            self.remoteFolder = '%s/sub-%s%s' % (self.currentTask['documentRoot'], self.currentTask['domainSub'], self.currentTask['domainFolder'])
        self.currentTask['doorLinksList'] = []
        
    def _CheckStatusCode(self):
        '''Проверить код статуса HTTP у залитого дора'''
        statusCode = urllib.urlopen(self.doorwayUrl).getcode()
        if statusCode != 200:
            raise Exception('Status code = %d' % statusCode)
        
    def _ActionOn(self):
        self._Settings()
        '''Запуск приложения'''
        self.doorgen = Doorgen(self.appTemplatesFolder, self.appTextsFolder, self.appSnippetsFolder)
        keywordsList = self.currentTask['keywordsList'][:]
        keywordsList.extend(self.currentTask['keywordsListAdd'])
        self.doorway = self.doorgen.Generate(keywordsList, self.currentTask['netLinksList'], self.currentTask['templateFolder'], len(self.currentTask['keywordsList']), self.doorwayUrl)
        self.doorway.UploadToFTP(self.currentTask['ftpHost'], self.currentTask['ftpLogin'], self.currentTask['ftpPassword'], self.remoteFolder)
        self.doorway.GooglePing()
        self._Done()
        self._Cron()
        return True
    
    def _ActionOff(self):
        #self._Settings()  # в текущей версии доргена это не нужно
        '''Значения по умолчанию'''
        self.currentTask['keywordsList'] = []
        self.currentTask['keywordsListAdd'] = []
        self.currentTask['netLinksList'] = []
        self.currentTask['doorLinksList'] = []
        '''Выходные параметры'''
        self.currentTask['doorLinksList'] = self.doorgen.pageLinksList[:]
        '''Проверяем код статуса (исключение не перехватывается)'''
        self._CheckStatusCode()
        return True

if __name__ == '__main__':
    agent = DoorgenMineAgent('http://searchpro.name/doorscenter/doorsadmin')
