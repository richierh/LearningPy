# this tutorial shows how to get variable within the class


class mytext(object):
    def onmytext(self):
        self.var = "hello"


running = mytext()
running.onmytext()
print running.var


class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var
        self.var = "hai semua"

foo = MyClass(2)
bar = MyClass(3)
print foo.class_var
print foo.i_var
print MyClass.class_var
MyClass(7)
print MyClass(7).var
