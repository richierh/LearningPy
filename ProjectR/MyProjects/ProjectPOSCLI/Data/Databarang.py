import dataset

def Databarangku(self):
    print ("Hahaha,Hello")
    db = dataset.connect('sqlite:///:memory:')

    table = db['sometable']
    table.insert(dict(name='John Doe', age=37))
    table.insert(dict(name='Ann Doe', age=34, gender='female'))

    self.besaran_brg=besaran_brg
    self.Jmlsatuan_brg =  Jmlsatuan_brg
    hasil(self)

    john = table.find_one(name='Ann Doe')
    print john



if __name__=="__main__":
    Databarangku(None)

