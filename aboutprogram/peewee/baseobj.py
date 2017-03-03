# /usr/bin/env python



class Base():
    print ("Oke, I am in baseobj.py file")
    def __init__(self):
        self.k = "k"

class C(Base):
    print ("hayo coba")
    def __init__(self):
        print ("ini adalah init")
        pass
    def cell(self):
        k = "hello"
        print (k)

C.cell("test")
