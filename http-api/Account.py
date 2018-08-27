import os
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId
import socket
import urllib2
import urllib


class Account_http():
    def __init__(self):
	self.url = "https://shanghai.51nebula.com:443/"
	
    def http_req(self, data):
    	data = json.dumps(data)
    	request = urllib2.Request(self.url)
    	request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
    	request.add_data(data) # post
    	# return  urllib2.urlopen(request).read()
	res = json.loads(urllib2.urlopen(request).read())
	return res

    def get_name(self, a): # a is a json here
	return a['result'][0]['name']
    def get_id(self, a): # a is a json here
    	return a['result']['id']
    def create_req_name(self, account_name):
	j = {}
	# {"jsonrpc": "2.0", "method": "get_account_by_name", "params": ["nathan"], "id": 1}
	j['jsonrpc'] = "2.0"
	j['method'] = "get_account_by_name"
	j['params'] = [account_name]
	j['id'] = 1
	return j
    def create_req_id(self, account_id):
	j = {}
	j['jsonrpc'] = "2.0"
	j['method'] = "get_accounts"
	j['params'] = [[account_id]]
	j['id'] = 1
	return j
    def get_name_with_id(self, account_id):
	c = self.create_req_id(account_id)
	j = self.http_req(c)
	return self.get_name(j)
    def get_id_with_name(self, account_name):
	c = self.create_req_name(account_name)
	j = self.http_req(c)
	return self.get_id(j)



if __name__ == "__main__":
    a = Account_http()
    print a.get_name_with_id('1.2.10160')
    print a.get_name_with_id('1.2.25')
    print a.get_name_with_id('1.2.7')
    print a.get_id_with_name('cletus-5')
    print a.get_id_with_name('nathan')

