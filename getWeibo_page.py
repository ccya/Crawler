# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup ,Comment

soup = BeautifulSoup(open('o2'))
usrlist = {}
weibolist = {}
link = []

### First get all the weibo content and corespondent user name and links

for node in soup.findAll('p',{'node-type':'feed_list_content'}):
    print node
    print "------"
    usr = node.a 
    usrname = usr['nick-name']
    u_link = usr['href']
    weibo = node.em.text
    usrlist[u_link] = usrname.encode('utf-8')
    weibolist[u_link] = weibo.encode('utf-8')
# print len(weibolist)

### get the nextpage link.
for node in soup.findAll('a',{'suda-data':'key=tblog_search_v4.1&value=weibo_page_1'}):
    if node.text == u'下一页': 
        next_page = node['href']
        next_page = 'http://s.weibo.com'+next_page
        link.append(next_page.encode('utf-8'))
print link
