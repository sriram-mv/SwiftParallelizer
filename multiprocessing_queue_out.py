import multiprocessing
import multiprocessing_import_worker_queue_out
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
    for i in range(8):
        p = multiprocessing.Process(target=multiprocessing_import_worker_queue_out.worker,args=(filename+'out',))
        jobs.append(p)
        p.start()