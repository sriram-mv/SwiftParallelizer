import requests
import io
import sys
import os
class User():
        def __init__(self, xauthtoken,xstoragetoken):
                # super(User, self).__init__()
                self.xauthtoken = xauthtoken
                self.xstoragetoken = xstoragetoken
                
def main():

        url='http://127.0.0.1:8080/auth/v1.0'
        # head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
        head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
        r=requests.get(url,headers=head)
        url12=r.headers['x-storage-url']
        containername=sys.argv[3]
        objectname=sys.argv[4]
        final_url = os.path.join(os.path.join(url12,containername),objectname)
        print final_url
        auth="AUTH"
        # print r.headers
        tester=User(r.headers.get('x-auth-token'),r.headers.get('x-storage-token'))
        # print tester.xauthtoken,tester.xstoragetoken
        test=tester.xauthtoken
        # print test
        if test == None:
                print "Wrong username or password"
                exit(1)
        if auth in test:
                
                print "Deleting"
                headers={"X-Auth-Token":tester.xauthtoken}
                r=requests.delete(final_url,headers=headers)
                print r.content
                print "Deleted!"

        else:
                print "Error Occured"
                exit(1)
        # url12='http://127.0.0.1:8080/v1/AUTH_test/images/dropbox.png'
        

if __name__ == '__main__':
        main()