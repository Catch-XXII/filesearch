import shutil
import time
import glob
import os
import time


class FileSeeker(object):
    def __init__(self):
        self.directory = input("Enter the directory: ")
        self.extension = input("Enter the extension: ")
        time.sleep(2)
        self.__str__()
        time.sleep(2)
        self.directory_change()
        self.search()
        self.file_mover()
        time.sleep(2)
        print("Check your desktop for result.txt")

    def __str__(self):
        print("I am looking for your {} files under the directory: {}".format(self.extension, self.directory))

    def directory_change(self):
        os.chdir(self.directory)

    def search(self):
            with open('result.txt', 'w+',encoding = 'utf-8') as f:
                for file in glob.glob(self.extension):
                    f.write(file+'\n')
                return f

    def file_mover(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        current_path = os.getcwd() + "\\" + "result.txt"
        shutil.move(current_path, desktop)
