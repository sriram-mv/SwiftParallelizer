# >>> import json
# >>> url = 'https://api.github.com/some/endpoint'
# >>> payload = {'some': 'data'}
# >>> headers = {'content-type': 'application/json'}

# >>> r = requests.post(url, data=json.dumps(payload), headers=headers)
# from requests.auth import AuthBase
import requests
import io
import os
import sys
import time
from read_xauth import xauth
class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
class User():
	"""docstring for User"""
	def __init__(self, xauthtoken,xstoragetoken):
		# super(User, self).__init__()
		self.xauthtoken = xauthtoken
		self.xstoragetoken = xstoragetoken
		
def main():
	with Timer() as t:
		xauth_token=xauth()
		test=xauth_token.split('\n')[0]
		xstorageurl=xauth_token.split('\n')[1]
		# url='http://127.0.0.1:8080/auth/v1.0'
	# head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
		# head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
		# r=requests.get(url,headers=head)
		url12=xstorageurl
		auth="AUTH"
		containername=sys.argv[3]
		objectpath=sys.argv[4]
		possibles = objectpath.split('/')
		objectname = possibles[len(possibles)-1]
		# print objectname
		
		final_url = os.path.join(os.path.join(url12,containername),objectname)
		# print final_url
	# print r.headers
		# tester=User(r.headers.get('x-auth-token'),r.headers.get('x-storage-token'))
		# print tester.xauthtoken,tester.xstoragetoken
		# test=tester.xauthtoken
	# print test
		if test == None:
			print "Wrong username or password"
			exit(1)
		if auth in test:
			# print "Uploadiing"
		#print r.headers
		# print len(r.content)
			xmlfile = open(objectpath, 'rb')
		# r = requests.put(url, data=xmlfile, headers=headers, auth=HTTPDigestAuth("*", "*")
			headers={"X-Auth-Token":test}
			# print url12
			r=requests.put(final_url,headers=headers,data=xmlfile)
			# print r.content
			# print "Uploaded!"
		
		else:
			print "Error Occured"
			exit(1)
	# url12='http://127.0.0.1:8080/v1/AUTH_test/images/dropbox.png'
	# print('Request took %.03f sec.' % t.interval)

if __name__ == '__main__':
	main()