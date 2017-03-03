# /usr/bin/env python

from firstplace import *

class lev1(Base):
    ar = L
    ar = "Has been change over here"
    print ("File inheritclass is over here")
    print (ar)
    pass

class lev2(lev1):
    print (lev1.ar)
    pass


import serial
ser = serial.Serial(port = '/dev/bus/usb/004/002')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()
