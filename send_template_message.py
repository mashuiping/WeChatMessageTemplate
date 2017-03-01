# coding=gbk

import httplib
import json
import ConfigParser
import sys

def send_template_message():
	template_data_info = {
				"first":"Hello mashuiping", 
				"keyword1":u"拿快递", 
				"keyword2":u"快递在明德园6号，密码*****，手机尾号8423", 
				"keyword3":u"高", 
				"keyword4":u"小林", 
				"remark":u"万分感谢"
	}
	config_info_file_path = 'config.txt'
	cf = ConfigParser.ConfigParser()
	cf.read(config_info_file_path)
	for app in cf.sections():
		access_token = cf.get(app, 'access_token')
	conn = httplib.HTTPConnection("api.weixin.qq.com:80")
	headers = {"Content-type":"application/json"}
	data = {     
				'touser':"odeOkwgSU0FZMq-yqoEFvgD4rij0",
				'template_id': "YblwjV2oEUtvhMVM1R0qTqrIHwJvKDMZtsKFr7iR5aU",
				'url':'http://www.baidu.com',
				'topcolor':'#FF0000',
				'data':{
					'first':{
						'value': template_data_info["first"],
						'color':'#173177'
					},
					'keyword1':{
						'value':template_data_info["keyword1"],
					    	'color':'#173177'
					},
					'keyword2':{
					 	'value':template_data_info["keyword2"],
					 	'color':'#173177'
					},
					'keyword3':{
						'value':template_data_info["keyword3"],
					    'color':'#173177'
					},
					'keyword4':{
					 	'value':template_data_info["keyword4"],
					 	'color':'#173177'
					},
					'remark':{
						'value':template_data_info["remark"],
						'color':'#173177'
					}
				}
		}    
	conn.request("POST", "/cgi-bin/message/template/send?access_token="+ access_token, json.JSONEncoder().encode(data), headers)
	response = conn.getresponse()
	data = response.read()
	if response.status == 200:
		print 'success'
        	print data
	else:
		print 'fail'
	conn.close()
if __name__ == '__main__':
	test()