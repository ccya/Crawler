import sys  
import re
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from PyQt4.QtNetwork import *
# -*- coding: utf-8 -*- 
  
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self) 
    url = QUrl.fromEncoded(url)
    self.useragent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    
####### The code below set a cookie jar for thie webpage   
    cookiebase = QNetworkCookie("","")
    self.cookies = cookiebase.parseCookies("")
    f = open("cookies_sina.txt")
    lines = f.readlines()
    tmphash = {}
    for line in lines:
        tmpl = line.split(":")
        if re.search("name",tmpl[0]):
            name = tmpl[1].rstrip("\n")
            name = name.rstrip(",")
            name = re.sub('"(.*?)"', r'\1', name)
        elif re.search("value",tmpl[0]):
            value = tmpl[1].rstrip("\n")
            value = re.sub('"(.*?)"', r'\1', value)
            tmphash[name] = value
            name = ""
            value = ""
    for each in tmphash.keys():
        cookietmp = QNetworkCookie(QByteArray(each),QByteArray(tmphash[each]))
        self.cookies.append(cookietmp)
        
####### The code below is to set the cookiejar to the networkmanager
    self.cookiejar = QNetworkCookieJar()
    self.cookiejar.setCookiesFromUrl(self.cookies, url)
    self.network_manager = QNetworkAccessManager()
    self.network_manager.setCookieJar(self.cookiejar)
    self.setNetworkAccessManager(self.network_manager)        

    self.loadFinished.connect(self._loadFinished) 
    self.mainFrame().load(url)
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'http://s.weibo.com/weibo/%25E6%2595%25B0%25E5%25AD%25A6%25E6%25BB%259A%25E5%2587%25BA%25E9%25AB%2598%25E8%2580%2583&page=2' 
r = Render(url)  
html = r.frame.toHtml()
print html.toUtf8()






