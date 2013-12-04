import marconi_queuing
import sys
import requests
import os
import uuid
class User():
    def __init__(self, xauthtoken,xstoragetoken):
        # super(User, self).__init__()
        self.xauthtoken = xauthtoken
        self.xstoragetoken = xstoragetoken

def main():
    custom_uuid = uuid.uuid4()
    url='http://127.0.0.1:8080/auth/v1.0'
    # head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
    head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
    r=requests.get(url,headers=head)
    url12=r.headers['x-storage-url']
    auth="AUTH"
    tester=User(r.headers.get('x-auth-token'),r.headers.get('x-storage-token'))
    # print tester.xauthtoken,tester.xstoragetoken
    container_name = sys.argv[3].split('.')[0]
    test=tester.xauthtoken
    if test == None:
            print "Wrong username or password"
            exit(1)
    if auth in test:
            # IntialPath=os.getcwd()
            # print "Showing Containers!"
            headers={"X-Auth-Token":tester.xauthtoken}
            r=requests.get(os.path.join(url12,container_name),headers=headers)
            objectlist = r.content.split('\n')
            del objectlist[len(objectlist)-1]
            marconi_queuing.create_queue(container_name+'out',custom_uuid)
            for _object in objectlist:
                body = marconi_queuing.request_body_queue(_object,os.path.join(os.path.join(url12,container_name),_object))
                message = [marconi_queuing.construct_json(body)]
                marconi_queuing.insert_messages(message,container_name+'out',custom_uuid)
            # marconi_queuing.delete_queue(sys.argv[3]+'out',custom_uuid)
if __name__ == '__main__':
    main()
