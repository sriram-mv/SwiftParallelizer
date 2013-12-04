import requests

class Connection():
	"""docstring for Connection"""
	def __init__(self, user, password):
		super(Connection, self).__init__()
		self.url ='http://127.0.0.1:8080/auth/v1.0'
		self.head={"X-Storage-User":user,"X-Storage-Pass":password}
		self.response = requests.get(url,headers=self.head)

	def get_xauthtoken(self):
		return self.response.get('x-auth-token')