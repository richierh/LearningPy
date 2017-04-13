#!/usr/bin/env python

import subprocess

def myfunction(Jawab):
    kliens= range (1,11)
    for klien in kliens :
        klien+1
        print klien

    Jawab =  raw_input("Silahkan masukkan nomor klien\n")
    #print Jawab
    #return Jawab

print myfunction(None)

def masukklien():
    subprocess.Popen()