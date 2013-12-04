import marconi_queuing
import uuid
from filesplit import file_splitter
import sys 
def files_in():
    return file_splitter.split_file(sys.argv[1])
    # print (filename, directory,part_fies)


def main():
    custom_uuid = uuid.uuid4()
    (filename, directory,part_files) =files_in()
    print filename
    new_filename=filename.split('.')
    final_filename = new_filename[0]
    marconi_queuing.create_queue(final_filename,custom_uuid)
    for part_file in part_files:
        body = marconi_queuing.request_body_queue(final_filename,part_file)
        message = [marconi_queuing.construct_json(body)]
        marconi_queuing.insert_messages(message,final_filename,custom_uuid)
    # marconi_queuing.delete_queue(final_filename,custom_uuid)

if __name__ == '__main__':
    main()