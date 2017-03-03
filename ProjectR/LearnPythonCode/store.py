from datetime import date
import createdb

def Personal(Person):
    uncle_bob = Person(name, birthday=date(1960, 1, 15), is_relative=True)
    uncle_bob.save() # bob is now stored in the database

if __name__=="__main__":
    name = "Bob"
    birthday =  date(1960,1,15)
    is_relative = True
    Personal(Person)
