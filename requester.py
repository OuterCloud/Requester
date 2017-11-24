import requests
from request_data import test_data
import json
import logging
from logging.config import fileConfig


class Logger(object):
	def __init__(self):
		fileConfig('logger.conf')
		self.logger = logging.getLogger('infoLogger')

	def info(self,info):
		self.logger.info(info)


class Requester(object):
	def __init__(self):
		self.test_data = test_data
		self.s = requests.Session()
		self.logger = Logger()

	def request(self,url,data,type):
		if type == "get":
			r = self.s.get(url,params=data)
			self.logger.info(r.text)
		elif type == "post":
			r = self.s.post(url,data=data)
			self.logger.info(r.text)

	def test(self,k):
		self.logger.info(k)
		v = self.test_data[k]
		self.request(type=v["type"],data=v["data"],url=v["url"])

	def test_all(self):
		for (k,v) in self.test_data.items():
			self.logger.info(k)
			self.request(type=v["type"],data=v["data"],url=v["url"])


if __name__ == '__main__':
	r = Requester()
	#r.test_all()
	r.test("查询登录状态接口")