# /usr/bin/env python

class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        self.alter = "okay"
        print "CHILD, BEFORE PARENT altered()"
        dad.altered()
        #super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()
dad.altered()
son.altered()
