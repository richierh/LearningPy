#!usr/bin/python

### Begin Coding ###


class Dataitem():
    #Class base
    def __init__(self,*args,**kwargs):
        self.b = args[0]
        self.a = kwargs
        return None        
    
    def hasil(self):
        for self.i in self.b:
            print self.i
    


if __name__=="__main__":
    lkodebrg = "1123345648"
    lnamabrg = "Sepatu Ariel"
    lsatuan  = "Buah"
    ljml     = "10"
    Dape=Dataitem([lkodebrg,lnamabrg,lsatuan],None)
    Dape.hasil()