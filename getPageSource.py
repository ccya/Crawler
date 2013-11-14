import urllib2
import sys
#from bs4 import BeautifulSoup ,Comment
# coding=utf-8
opener = urllib2.build_opener()
opener.addheaders = [('Accept-Charset','utf-8')]
#link = 'http://s.weibo.com/weibo/%25E6%2595%25B0%25E5%25AD%25A6%25E6%25BB%259A%25E5%2587%25BA%25E9%25AB%2598%25E8%2580%2583&b=1&page=2'
# request = urllib2.Request(link)
link = 'http://us.weibo.com/gb'
response = opener.open(link)
page_source = response.read().decode('utf-8')
# encode_type = sys.getfilesystemencoding()
# html = unicode(page_source, 'utf-8')
# print page_source.encode('utf-8')
charset = response.headers.getparam('charset')
print unicode(page_source).encode('utf-8')
