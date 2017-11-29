from iqoptionapi.api import IQOptionAPI
import iqoptionapi.constants as api_constants
import time
import os
import threading

#http://localhost:8001?value=2&active=EURUSD-OTC&t=1&op=put
#http://localhost:8001?value=3&active=EURUSD&t=3&op=call

class myThread (threading.Thread):
   def __init__(self, threadID, name, value ,active,t,op):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.value = value
      self.active = active
      self.t = t
      self.op = op ## put call
      self.api  = IQOptionAPI("iqoption.com", "b418@gmail.com", "b418b418")
   def run(self):
      print "Starting " + self.name
      start(self.value,self.active,self.t,self.op,self.api);
      #print_time(self.name, 5, self.counter)
      print "Success " + self.name


 

def start(value,active,t,op,api_):
	#api_ = IQOptionAPI("iqoption.com", "b418@gmail.com", "b418b418")
	api_.status = 'start'; 
	api_.loop=1
	#api.active = "EURUSD-OTC" "EURUSD"
	api_.active = active #"EURUSD"
	api_.last = '='; #win lose
	api_.connect() 
	#api.change_balance('practice'); 
	#api.candles(1, 1)
	#"EURUSD-OTC": 76,
	api_.setactives([api_constants.ACTIVES[api_.active]])
	 
	api_.timesync.expiration_time = int(t)
	#api.setactives([1,2])
	# candles = api.getcandles(76, 1)
	trade(api_,value,api_constants.ACTIVES[api_.active],op);
	# api.timesync.expiration_time = 1
	time.sleep(2)
	#api.buy(1, 76, "turbo", "call")

 

def cl():
	os.system('cls' if os.name=='nt' else 'clear')


def trade(api__,value,active,op):
	cl()
	 
	api__.status =   'calling';
	while True:
		api__.loop = api__.loop+1
		if api__.loop>80:
			break
		print api__.timesync.server_datetime 
		print op+":"+"trading... "+str(api__.loop)
		if api__.status ==  'calling':
			print "calling"
			api__.status ==  'waitcall';
			api__.buy(value, active, "turbo", op)
			time.sleep(1)
		if api__.status ==  'called':
			break
		#print "tradestatus "+api.status
		time.sleep(1)
		cl()
	cl()
	 


# while True:
# 	#print api.timesync.server_datetime.second
# 	cl()
# 	print api.timesync.server_datetime
# 	print "status "+api.status +" last "+api.last
# 	if (api.last == '=') and (api.status !=  'called'): #(api.status == 'start') or 
# 		trade();
# 	if (api.last == 'win') or (api.last == 'loose'):
# 		api.status = 'start'; 
# 		api.last = '=';
# 	time.sleep(1)
	# 	if 	api.timesync.server_datetime.second < 20 :
	# 		api.buy(1, 76, "turbo", "call")
	# 		break
	# 	else:
		 
	#while not api.timesync.server_datetime.second > 20:
	#	print "call"
	#	api.buy(1, 76, "turbo", "call")
	#	time.sleep(1)
	#print api.profile
	 

import random
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        import os
        r = random.randint(1,101)
         

        value = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('value', None)
        active = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('active', None)
        t = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('t', None)
        op = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('op', None)
        if t[0] != "exit" and ( op[0] == 'put' or op[0] == 'call' ):
        	thread1 = myThread(  r, r ,value[0],active[0],t[0],op[0])
        	thread1.start()
        else:
        	httpd.server_close()

 		# if t[0] != "exit" :
			# thread1 = myThread(  r, r ,value[0],active[0],t[0])
			# thread1.start()
		# Prints None or the string value of imsi

        #os.startfile("C:\streams.json")
        #start();
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        

server_address = ('', 8001)
httpd = HTTPServer(server_address, S)
def run(server_class=HTTPServer, handler_class=S, port=8001):
     
    import os
    os.system('cls')
    print 'Starting API@127.0.0.1:8001 v0.02'
    print 'Call @ http://localhost:8001?value=2&active=EURUSD&t=1&op=call'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


# {"name":"listInfoData","msg":[{"amount":1000000,"id":3546083402,"refund":0,"curr
# ency":"USD","currency_char":"$","active_id":76,"active":"EURUSD-OTC","value":1.1
# 93147,"exp_value":1193129,"dir":"call","created":1511595610,"expired":1511595660
# ,"type_name":"turbo","type":"front.TU","profit":0,"profit_amount":0,"win_amount"
# :1.83,"loose_amount":0,"sum":1,"win":"loose","now":1511595660,"user_id":12522841
# ,"game_state":1,"profit_income":183,"profit_return":0,"option_type_id":3,"site_i
# d":1,"is_demo":true,"user_balance_id":16331670,"client_platform_id":4,"re_track"
# :null,"params":null,"rate_finished":true}]}



		 