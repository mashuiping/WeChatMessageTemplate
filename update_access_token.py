import ConfigParser
import httplib
import json
from time import sleep

class update_access_token(object):
	"""docstring for update_access_token"""
	def __init__(self):
		super(update_access_token, self).__init__()
		self.conn = httplib.HTTPSConnection("api.weixin.qq.com:443")
		self.config_info_file_path = 'config.txt'
		self.cf = ConfigParser.ConfigParser()
		self.cf.read(self.config_info_file_path)
		for app in self.cf.sections():
			self.app_id = self.cf.get(app, 'app_id')
			self.app_secret = self.cf.get(app, 'app_secret')
			self.access_token = self.cf.get(app, 'access_token')

	def access_token_geter(self):
		try:
			url = "/cgi-bin/token?grant_type=client_credential&appid=" + self.app_id + "&secret=" + self.app_secret
			self.conn.request('GET', "/cgi-bin/token?grant_type=client_credential&appid=" + self.app_id + "&secret=" + self.app_secret)
			response = self.conn.getresponse()
			print response.status
			print response.reason
			json_data = response.read()
			self.access_token = json.loads(json_data)["access_token"]
			self.access_token_updater()
		except Exception as e:
			print e
		finally:
			if self.conn:
				self.conn.close()
	def access_token_updater(self):
		self.cf.set("app", 'access_token', self.access_token)
		app_config = open(self.config_info_file_path, 'w')
		self.cf.write(app_config)
		app_config.close()
if __name__ == '__main__':
	while 1:
		my_updata_access_token = update_access_token()
		my_updata_access_token.access_token_geter()
		sleep(5400)                                          #update per one half and a hour