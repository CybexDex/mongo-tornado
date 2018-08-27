import os
from tornado import ioloop,web
from tornado.escape import json_encode
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId
import socket
import websocket
from websocket import create_connection
import urllib2
import urllib
import Account as act
 
def ws_inst():
    ws = create_connection("wss://shanghai.51nebula.com/", timeout=5)
    if ws.connected:
    	ws.send('{"id": 1, "method": "call", "params": [1, "login", ["",""]]}', opcode=websocket.ABNF.OPCODE_TEXT)
    	print ws.recv()
    	ws.send('{"id": 2, "method": "call", "params": [1, "history", []]}', opcode=websocket.ABNF.OPCODE_TEXT)
    	print ws.recv()
    return ws

def http_req(data):
    request = urllib2.Request("https://shanghai.51nebula.com:443/")
    request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
    # return  urllib2.urlopen(request, urllib.urlencode(data)).read()
    return  urllib2.urlopen(request, urllib.urlencode(data)).read()



MONGODB_DB_URL = os.environ.get('OPENSHIFT_MONGODB_DB_URL') if os.environ.get('OPENSHIFT_MONGODB_DB_URL') else 'mongodb://yoyo:yoyo123@39.105.55.115:27017/cybex'
MONGODB_DB_NAME = os.environ.get('OPENSHIFT_APP_NAME') if os.environ.get('OPENSHIFT_APP_NAME') else 'cybex'

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")
class accIdHandler(web.RequestHandler):
    def get(self, accid):
	a = act.Account_http()
	res = [ a.get_name_with_id(accid) ]
	self.write(json.dumps(res, default=json_util.default))
class accNameHandler(web.RequestHandler):
    def get(self, accname):
	a = act.Account_http()
	res = [ a.get_id_with_name(accname) ]
	self.write(json.dumps(res, default=json_util.default))


class accountHandler(web.RequestHandler):
    def pending(self, account_name, limit):
        ws = ws_inst()
	req = '{"id": 3, "method": "call", "params": [2, "get_account_history", [ "%s" ,"1.11.0", %d , "1.11.0"]]}' % (account_name , limit)
	print req
	ws.send(req, opcode=websocket.ABNF.OPCODE_TEXT)
	res = ws.recv()
	self.write("\n--------------------------------------pending in node----------------------------------------\n")
	self.write(res)
        ws.close()
    def get(self,account_name):
        account_history = db.account_history.find({'account_history.account':account_name}).sort([('block_data.block_num',-1)] ).limit(100)
        self.set_header("Content-Type", "application/json")
	self.pending(account_name, 100)
	self.write("\n--------------------------------------lib in mongo----------------------------------------\n")
        self.write(json.dumps(list(account_history),default=json_util.default))
    # def post(self,account_name, _skip, _limit):
    def post(self, account_name , *args, **kwargs):
	# print self.request
	_skip = int(self.get_argument('skip',None))
	_limit = int(self.get_argument('limit',None))
        # account_history = db.account_history.find({'account_history.account':account_name}).skip(_skip).limit(_limit)
        account_history = db.account_history.find({'account_history.account':account_name}).sort([('block_data.block_num',-1)] ).skip(_skip).limit(_limit)
        # account_history = db.account_history.find({'account_history.account':account_name}).sort({'account_history.account':-1} ).skip(_skip).limit(_limit)
        self.set_header("Content-Type", "application/json")
	self.pending(account_name, 100)
	self.write("\n--------------------------------------lib in mongo----------------------------------------\n")
        self.write(json.dumps(list(account_history),default=json_util.default))
        


class blockHandler(web.RequestHandler):
    def pending(self, block_num):
	res = http_req({"jsonrpc": "2.0", "method": "get_block", "params": [ block_num ], "id": 1})
	print res
	return res
    def get(self , block_num):
	block_num = int(block_num)
	# self.write(self.pending(block_num))
	# return 
        # story = db.account_history.find_one({"_id":ObjectId(str(story_id))})
        block = db.account_history.find_one({'block_data.block_num': block_num })
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps((block),default=json_util.default))


settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True
}

application = web.Application([
    (r'/', MainHandler),
    (r'/index', IndexHandler),
    (r'/api/v1/account_id/(.+)', accIdHandler),
    (r'/api/v1/account_name/(.+)', accNameHandler),
    (r'/api/v1/account_history/(.+)',accountHandler),
    (r'/api/v1/block_num/(\d+)', blockHandler)
],**settings)


if __name__ == "__main__":
    print settings
    application.listen(8081)
    ioloop.IOLoop.instance().start()
