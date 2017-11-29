from datetime import datetime
import urllib2,time,os


def getExp(html):
	 
	html = html.split('expiry at <script>document.write(ShowLocalTime(')
	html = html[1]
	html = html.split('));')
	exp = html[0]
	return exp

def getOp(html):
	html = html[1]
	html = html.split('\\n')
	html = html[0]
	op = html[-2:-1]
	return op

os.system('cls')
last = '0'
target = 'https://binary-signal.com/en/chart/eurusd'
#target = 'https://binary-signal.com/en/chart/eurusd/?ts=1511856900';
base = 'http://localhost:8001?value=2&active=EURUSD'
while True:
	os.system('cls')
	print str(str(datetime.now()))+" v0.02"  #str(datetime.now())
	#print email +":"+ password
	#print "status:"+api.status 	
	print "calling ... " + target
	if True :
		response = urllib2.urlopen(target)
		html = response.read()
		exp = getExp(html)
		#ts = time.time()
		ts = str(  ( ( int(exp)-int(time.time())) / 60  ) +1)
		print "EXP "+exp+' '+str(datetime.fromtimestamp(int(exp))) + " " + str(ts) + " Min" 
		html = html.split('\\nS')
		#print len(html)
		if ( (len(html) > 1) and (exp!=last)  ):		 
			 
			op = getOp(html) 
			if op == '-' :
				op = "put"
			if op == '+' :
				op = "call"
				
			if (op == 'put' or  op == 'call'):

				if int(ts)>5:
					ts = "5"
				url =  base+"&t="+ts+"&op="+op
				print op+": "+url
				try:
					print "call ... "+url
					response = urllib2.urlopen(url)
					last = exp
				#r = random.randint(1,101)
					#thread1 = myThread(  r, r ,value,active ,t ,op )
					#thread1.start()
				#start(value,active,t,op)

				except Exception:
					print "can't call "+url

		else:
			print "wait" 
 
	time.sleep(2)
	 


	 # from datetime import datetime
# import urllib2,time,os
 
# while True:
# 	response = urllib2.urlopen('http://www.baccarat369.com/new/bs.php')
# 	html = response.read()
# 	#os.system('cls')
# 	print str(datetime.now())
# 	print html
# 	if html != 'wait' and  html != '':
# 		response = urllib2.urlopen('http://localhost:8001?value=2&active=EURUSD&t=1&op='+html)
		 
# 	time.sleep(1)
	 
 