import os
import subprocess
import time
def split_file(filename):
    os.chdir(os.path.join('/home/sriram/SpecialProblem','Objects'))
    if filename in  os.listdir(os.getcwd()):
        # print filename
        # filename = os.listdir(os.getcwd())
        directory = filename.split('.')[0]
        # print directory
        os.mkdir(directory)
        subprocess.call('split -b 50k '+filename+' part',shell=True)
        # time.sleep(1)
        subprocess.call('mv part* '+directory,shell=True)
        os.chdir(directory)
        # print os.getcwd()
        part_files=[]
        for files in os.listdir(os.getcwd()):
            part_files.append(os.path.abspath(files))
        # subprocess.check_output()
        return (filename,os.path.abspath(directory),part_files)
        


def main():
    print split_file()
    

if __name__ == '__main__':
    main()