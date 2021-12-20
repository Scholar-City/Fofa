#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Saint Michael
# @FileName: Fofa_Query.py

import configparser
import datetime
import requests
import base64
import json

class Fofa:
	email = ''
	api = ''
	keyword = ''
	page = ''
	size = ''
	lis = []
	def __init__(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		self.email = config.get('fofa_config','email')
		self.api = config.get('fofa_config','api')
		self.keyword = config.get('fofa_config','keyword')
		self.page = config.get('fofa_config','page')
		self.size = config.get('fofa_config','size')

	def Request(self):
		lis = []
		url = 'https://fofa.so/api/v1/search/all?email={0}&key={1}&qbase64={2}&page={3}&size={4}'.format(self.email,self.api,self.keyword,self.page,self.size)
		headers = {
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
		}
		try:
			response = requests.get(url=url,headers=headers)
			text = json.loads(response.text)
			for i in range(len(text['results'])):
				lis.append(text['results'][i][0])
			self.lis = list(set(lis))
			return self.lis
		except:
			pass

	def Write_Url(self):
		name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		f = open('%s.txt' % (name), 'a', encoding='utf-8')
		for url in self.lis:
			if not 'http' in url:
				url = 'http://' + url
			f.write(url + '\n')
			print(url)

if __name__ == '__main__':
	fofa = Fofa()
	fofa.Request()
	fofa.Write_Url()
