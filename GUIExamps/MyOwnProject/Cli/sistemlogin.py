#!usr/bin/env python

##Making system login

import time
import sys

class Sistim_login():
    
    def tambah_pengguna(self,simpan):
        pengguna = raw_input('Masukkan Nama pengguna: ')
        sandi = raw_input('Masukkan sandi: ')
        if pengguna in Pustaka_global:
            print "Nama pengguna atau sandi sudah dipakai"
            return False
        else:
            simpan[pengguna] = sandi
            return True
        #and call this 10 times for example...
    
    def __init__(self):
        Pustaka_global = dict()
        print "Proses berjalan, persiapan awal program\n"
        i = 1
        while i <= 5:
            print "%d \r"%i,
            sys.stdout.flush()
            time.sleep(1)
            i=i+1
        print "\nSelesai.......Terima kasih telah menunggu"
        while True:
            print ("Pilih\n"
                   "1.\n"
                   "2.\n"
                   "3.\n"
                   "4.\n")
            self.jwbn =raw_input("")
            if self.jwbn==str(4):
                break
            self.add_user(Pustaka_global)
        

if __name__=="__main__":
    mylogin = loginsystem()
  