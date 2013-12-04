import io,sys,os
import requests
from collections import defaultdict
def ensure_dir(f):
        if not os.path.exists(f):
                try:
                        os.makedirs(f)
                except OSError as exception:
                        if exception.errno != 17:
                                raise
class User():
        def __init__(self, xauthtoken,xstoragetoken):
                # super(User, self).__init__()
                self.xauthtoken = xauthtoken
                self.xstoragetoken = xstoragetoken
class Paths():
        def __init__(self,normalpath,containerpath,objectpath):
                self.normalpath=normalpath
                self.containerpath=containerpath
                self.objectpath=objectpath
def main():
        FinalSyncList=defaultdict(list)
        url='http://127.0.0.1:8080/auth/v1.0'
        # head={"X-Storage-User":"test:tester","X-Storage-Pass":"testing"}
        head={"X-Storage-User":sys.argv[1],"X-Storage-Pass":sys.argv[2]}
        r=requests.get(url,headers=head)
        url12=r.headers['x-storage-url']
        auth="AUTH"
        tester=User(r.headers.get('x-auth-token'),r.headers.get('x-storage-token'))
        # print tester.xauthtoken,tester.xstoragetoken
        test=tester.xauthtoken
        # print test
        if test == None:
                print "Wrong username or password"
                exit(1)
        if auth in test:
                IntialPath=os.getcwd()
                # print "Showing Containers!"
                headers={"X-Auth-Token":tester.xauthtoken}
                r=requests.get(url12,headers=headers)
                # print r.content
                Containerlist=r.content.split('\n')
                # print Containerlist
                size=len(Containerlist)-1
                ContainerIter=iter(Containerlist)
                while size>0:
                        ensure_dir(os.getcwd()+'/'+sys.argv[1]+'/'+ContainerIter.next()+'/')

                        size=size-1
                Containersize=len(Containerlist)-1
                ContainerIter=iter(Containerlist)
                Objectsize=0
                while Containersize>0:
                        container=ContainerIter.next()                        
                        r=requests.get(url12+'/'+container+'/',headers=headers)
                        # print 'Objects inside ',container
                        Objectlist=r.content.split('\n')

                        
                        print Objectlist
                        Objectsize=len(Objectlist)-1

                        ObjectIter=iter(Objectlist)

                        while Objectsize>0:
                                Object=ObjectIter.next()
                                # print url12
                                # print container
                                # print Object
                                FinalSyncList[container].append(Object)
                                print os.getcwd()
                                q=requests.get(url12+'/'+container+'/'+Object,headers=headers)
                                fh=open(os.getcwd()+'/'+sys.argv[1]+'/'+container+'/'+Object,'wb+')
                                # fh=open(file_name,'rb')
                                fh.write(q.content)
                                fh.close()
                                # print os.getcwd()
                                # print q.content
                                # if container in os.getcwd()
                                # os.chdir(os.getcwd()+'/'+sys.argv[1]+'/'+container+'/')
                                # print os.getcwd()        
                                Objectsize=Objectsize-1
                        # os.chdir("../")
                        Containersize=Containersize-1
        print FinalSyncList        
if __name__ == '__main__':
        main()