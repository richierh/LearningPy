#f = open("/home/richie/Documents/Baca.txt")
#for line in f:
#    print line
#f.close()
#the open keyword opens a file in read-only mode by default

#import required module to open a file from its own program
import subprocess

#this is a path for the data that are going to be opened
ods = "/home/pmc/Documents/Data.ods"

#below is the source of executables libreoffice 
sofficebin =r'/usr/lib/libreoffice/program/soffice.bin'
subprocess.Popen([sofficebin,ods])


#f = file("/home/richie/Documents/Baca.txt")
# read all the lines in the file and return them in a list
#lines = f.readlines()
#print lines
#f.close()
