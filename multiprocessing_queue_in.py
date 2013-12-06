import multiprocessing
import multiprocessing_import_worker_queue_in
import sys
# def worker(num):
#     """thread worker function"""
#     print 'Worker:'
#     return
def get_file(filename):
    return filename.split('.')[0]
if __name__ == '__main__':
    filename = get_file(sys.argv[1])
    jobs = []
    number_threads = int(sys.argv[2])
    for i in range(number_threads):
        p = multiprocessing.Process(target=multiprocessing_import_worker_queue_in.worker,args=(filename,))
        jobs.append(p)
        p.start()