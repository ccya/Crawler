# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup ,Comment
soup = BeautifulSoup(open('weibo_html'))
usrlist = {}
weibolist = {}
c = 0
for elm in soup.findAll('em', {'node-type': 'txt_em'}):
    usr = elm.previousSibling.previousSibling
    usrname = usr.text
    uid = usr['action-data']
    weibo = elm.text
    # print 'new'
    # print uid
    # print usrname.encode('utf-8')
    # print weibo.encode('utf-8')
    # print '---------'
    usrlist[uid] = usrname.encode('utf-8')
    weibolist[uid] = weibo.encode('utf-8')

print usrlist.keys()
print weibolist.keys()
