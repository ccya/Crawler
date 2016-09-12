import urllib2
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
		
	def vote(ip):
		

