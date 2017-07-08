# /usr/bin/env python
# -*- coding:utf-8-*-
# Membuat Model MVC

class myview():
    def __init__(self):
        self.a = raw_input (" Silahkan pilih\n Trending Topik pilihanmu \n 1. om Telolet om \n 2. PPAP (Pen Pineapple Apple Pen)\n 3. Smule Challenge\n")
    pass

class mymodel():
    pass

class mycontroller(myview):

    def __init__(self,a):
        self.parent =  a
        print l.a

    pass


l =  myview()
mc = mycontroller("satu")
