from connection import Connection
import sys

def main():
    with open('swift_xauth.conf','w+') as swift_open:
        get_connection = Connection(sys.argv[1],sys.argv[2])
        auth_token = get_connection.get_xauthtoken()
        xstorageurl = get_connection.get_storage_url()
        swift_open.write(auth_token+'\n')
        swift_open.write(xstorageurl)

if __name__ == '__main__':
    main()