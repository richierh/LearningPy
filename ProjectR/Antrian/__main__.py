21#!/usr/bin/python
# -*- coding: utf-8 -*-
class antrian(object):

    def __init__(self,pencet):
        super(antrian,self).__init__()
        self.pencet = pencet
        self.tombol()

    def tombol(self):
        with open('mydata.txt', 'w') as f:
            for iter in range (1,10):
            #read_data = f.read()
                write_data = f.write(iter)
                iter = iter+1
                print write_data
            #print read_data
                f.close()



if __name__ == "__main__":
    print ("hello")
    pencet =  input("Silahkan tekan antrian\n")
    antrian(object)