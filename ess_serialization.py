import os
import pickle

class A:
    def __init__(self, name, filename, lst=None, dic=None):
        if os.name == 'posix':
            FILE_PATH = "/sdcard/"  # if executed on Android
        else:
            FILE_PATH = "D:/development/python/"  # if executed on Windows
    
        self.name = name
        self.filePathName = FILE_PATH + filename

        if not lst and not dic:
            self.lst = None
            self.dic = None
            self.deserialize()
        else:
            self.lst = lst
            self.dic = dic

    def serialize(self):
        print('serializing ' + self.name)

        with open(self.filePathName, 'wb') as f:
            pickle.dump(self.lst, f, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.dic, f, pickle.HIGHEST_PROTOCOL)

    def deserialize(self):
        print('deserializing ' + self.name)

        try:
            with open(self.filePathName, 'rb') as f:
                self.lst = pickle.load(f)
                self.dic = pickle.load(f)
        except FileNotFoundError as e:
            print(e)

if __name__ == '__main__':
    a = A('a', 'serialize.bin', ['a','b','c'], {'a':1, 'b':2, 'c':3})
    print(a.lst)
    print(a.dic)
    a.serialize()
    aa = A('aa', 'serialize.bin')
    print(aa.lst)
    print(aa.dic)
