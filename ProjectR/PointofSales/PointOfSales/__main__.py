#! usr/bin/env python
# This is the script for input data

class DB():
    def __init__(self):
        #This is the places for all the initiate
        self.kodeID = raw_input("masukkan no ID\n")        
        self.Nama = raw_input("masukkan Nama\n")
        self.JenisK = raw_input("masukkan Jenis Kelamin\n")
        self.alamat = raw_input("masukkan alamat\n")
        self.notel = input("masukkan no telp/hp\n")
        
    def get(self):
        #We get all the information from __init__
        for i in [self.kodeID,self.Nama,
                  self.JenisK,self.alamat,
                  self.notel]:
            print i

if __name__=="__main__":
    #This is the main program that is being executed first
    print "Hello,Selamat Datang silahkan\nisi data dibawah ini"
    db = DB()
    db.get()
    