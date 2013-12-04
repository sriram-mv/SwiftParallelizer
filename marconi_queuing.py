import requests
import json
import sys
import uuid
from marconi.tests.functional import helpers
# from endpoints import IDENTITY_URL,MARCONI_URL
# from authentication import auth
MARCONI_URL = 'http://127.0.0.1:8888/v1/queues/'

# Create Queue
def create_queue(queue_name,custom_uuid):

    Final_URL = MARCONI_URL+'{0}'.format(queue_name)
    _headers={'Client-ID':str(custom_uuid)}
    response = requests.put(Final_URL,verify=False,headers=_headers)
    # print response.headers,response.content,response.status_code
# Delete Queue
def delete_queue(queue_name,custom_uuid):
    # XAuthToken = response['access']['token']['id']
    Final_URL = MARCONI_URL+'{0}'.format(queue_name)
    _headers={'Client-ID':str(custom_uuid)}
    response = requests.delete(Final_URL,verify=False,headers=_headers)
    # print response.headers,response.content,response.status_code

# Insert Messages into the Queue

def insert_messages(data,queue_name,custom_uuid):
    # XAuthToken = response['access']['token']['id']
    URL = MARCONI_URL+'{0}/messages'.format(queue_name)
    _headers={'Client-ID':str(custom_uuid)}
    # print data
    # print type(data)
    response=requests.post(URL,data=json.dumps(data),headers=_headers)
    # print response.headers,response.content,response.status_code
# Claim Messages
def claim_messages(custom_uuid,data,queue_name,limit):
    # XAuthToken = response['access']['token']['id']
    URL = MARCONI_URL+'{0}/claims?limit={1}'.format(queue_name,limit)
    _headers={'Client-ID':str(custom_uuid)}
    # _headers={'content-type': 'application/json','Client-ID':'PingPongBot','X-Auth-Token':XAuthToken,'X-Project-Id':234}
    response = requests.post(URL,data=str(data),headers=_headers,verify=False)
    # print q.headers,q.content,q.status_code
    if response.status_code != 204:
        data = response.json()
        print data
        message = json.loads(json.dumps(data[0]))
        firstsplit = message['href'].split('/')
        second_split = firstsplit[len(firstsplit)-1].split('?claim_id=')
        # message id followed by claim id
        print second_split[0], second_split[1]
        return (message['body'],second_split[0],second_split[1])
    else:
        return (response.status_code,0,0)
        print (response,'0','0',response.status_code)

# Delete Message with claim
def delete_messages_with_claim(custom_uuid,message_ids,queue_name,claim_id):
    # XAuthToken = response['access']['token']['id']
    URL = MARCONI_URL+'{0}/messages/{1}?{2}'.format(queue_name,message_ids,claim_id)
    # _headers={'content-type': 'application/json','Client-ID':'PingPongBot','X-Auth-Token':XAuthToken,'X-Project-Id':234}
    _headers={'Client-ID':str(custom_uuid)}
    response = requests.delete(URL,headers=_headers,verify=False)
    # print response.headers,response.content,response.status_code

def delete_claim(custom_uuid, claim_id, queue_name):
    # XAuthToken = response['access']['token']['id']
    URL = MARCONI_URL+'{0}/claims/{1}'.format(queue_name,claim_id)
    # _headers={'content-type': 'application/json','Client-ID':'PingPongBot','X-Auth-Token':XAuthToken,'X-Project-Id':234}
    _headers={'Client-ID':str(custom_uuid)}
    response = requests.delete(URL,headers=_headers,verify=False)
    # print response.headers,response.content,response.status_code

def request_body(event,vs,time):
    body = {'event':event,
            'vs':vs,
            'time':time}
    message = {'body' : body,
               'ttl' : 100}
    return [message]

def request_body_splitfile(filename,filelocation):
    body = {'filename':filename,
            'filelocation':filelocation}
    message = {'body': body,
               'ttl': 100}
    return [message]
def request_body_queue(filename,filelocation):
    body = {'filename':filename,
            'filelocation':filelocation}
    return body
def construct_json(body1):
    message = {'body' : body1,
               'ttl' : 100}
    return message

def for_claim():
    data = {'ttl':100,'grace':100}
    return json.dumps(data)

    
# def main():
    
#     # body = {}
#     message_list=[]
#     custom_uuid = uuid.uuid4()
#     create_queue('sriram',custom_uuid)
#     body1 = {'awesome':'True'}
#     body = construct_json(body1)
#     message_list.append(body)
#     # message_list = helpers.create_message_body(messagecount=1)
#     insert_messages(message_list,'sriram',custom_uuid)
#     (message_id,claim_id) = claim_messages(custom_uuid,for_claim(),'sriram')
#     delete_messages_with_claim(custom_uuid,message_id,'sriram',claim_id)
#     delete_queue('sriram',custom_uuid)

# if __name__ == '__main__':
#     main()