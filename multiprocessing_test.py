import multiprocessing
import multiprocessing_import_worker
# def worker(num):
#     """thread worker function"""
#     print 'Worker:'
#     return

if __name__ == '__main__':
    jobs = []
    for i in range(3):
        p = multiprocessing.Process(target=multiprocessing_import_worker.worker,args=('sriram_1',))
        jobs.append(p)
        p.start()