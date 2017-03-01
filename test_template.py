import extern_variate
import httplib
import json

class  test_template(object):
	"""docstring for  test_template"""
	def __init__(self, arg):
		super( test_template, self).__init__()
		self.app_id = app_id
		self.app_secret = app_secret
		self.access_token = access_token
		self.conn = httplib.HttPConnection("api.weixin.qq.com:80")
		self.headers = {"Content-type":"application/json"}

	def GET(self):
		try:
			data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "first_template_message"
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                self.POST
            else:
                return ""
        except Exception, Argument:
            return Argument

	def send_template_message(data):
		requrl = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + self.access_token
		send_data = self.conn.request("POST", "/cgi-bin/message/template/send?access_token="+ self.access_token, data, self.headers)
		response = conn.getresponse()
		data = response.read()
		if response.status == 200:
			print 'success'
			print data
		else:
			print 'fail'
		conn.close()

	def data_generater(self):
		data = {     
				'touser':"odeOkwgSU0FZMq-yqoEFvgD4rij0",
				'template_id':'OC5mXIJ1_Gubv-ftvxHjMEXqzQ8P8FMvpdeGv2zBpKU',
				'url':'',
				'topcolor':'#FF0000',
				'data':{
					'first':{
						'value':'succeed',
						'color':'#173177'
					},
					'keyword1':{
						'value':'cookie',
					    'color':'#173177'
					},
					'keyword2':{
					 	'value':'39.8',
					 	'color':'#173177'
					},
					'keyword3':{
						'value':'cookie',
					    'color':'#173177'
					},
					'keyword4':{
					 	'value':'39.8',
					 	'color':'#173177'
					},
					'remark':{
						'value':'welcome to next time!',
						'color':'#173177'
					}
				}
		}
		return data

	def POST(self):
		try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            	toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
		return send_template_message(data_generater())
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment

		