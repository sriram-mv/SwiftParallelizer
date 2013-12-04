import marconi_queuing
import uuid
import subprocess
def worker(queuename):
    
    # body['filename']
    # body['filelocation']
    while True:
        (body, message_id,claim_id) = marconi_queuing.claim_messages(uuid.uuid4(),marconi_queuing.for_claim(),queuename,1)
        print body
        print message_id
        print claim_id
        if body==204:
            return
        else:
            shell_script = 'python getobject.py test:tester testing {0}'.format(body['filelocation'])
            print body['filename']
            print body['filelocation']
            subprocess.call(shell_script,shell=True)
            marconi_queuing.delete_messages_with_claim(uuid.uuid4(),message_id,queuename,claim_id)



    # print queuename
    # print 'Worker {num}'.format(num=num)
