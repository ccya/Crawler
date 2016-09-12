import urllib2
import random
from BeautifulSoup import BeautifulSoup
class VoteBot:
	self.proxySource = "http://proxy.com.ru/"
	self.proxyList = []
	
	def getProxy():
		req = urllib2.Request(self.proxySource)
		try: 
			response = urllib2.urlopen(req)
			html = response.read()
			soup = BeautifulSoup(html)
			proxyTable = soup.body.center.font.table.tbody.tr.td[1].font.table.tbody
			rows = proxyTable.find_all('tr')
			for i in xrange(1,len(rows)):
				cols = row.find_all('td')
				ip = cols[0] + ":" + cols[1]
				self.proxyList.append(ip)
		except URLError as e:
			print e.reason
		//email me?
			quit()
		
	def constructHeaders():
		user_agents = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWe。。。hrome/45.0.2454.101 Safari/537.36",
		"Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.。。。。likeGecko) Chrome / 45.0.2454.101Safari/ 537.36",
		"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit。。。。。Gecko) Chrome/50.0.2661.102 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3。。。。ML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
		"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) 。。。WebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
		"User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKi。。。。。36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
		"Mozilla/5.0 (Windows NT 10.0; WOW64) Apple。。。。。KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
		] 
		
//http://blog.csdn.net/qq_29883591/article/details/52016802
//http://outofmemory.cn/code-snippet/1653/python-pachong-zhua-wangye-summary
		
		
	def vote(ip):
		

