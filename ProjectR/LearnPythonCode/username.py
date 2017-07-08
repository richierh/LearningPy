# /usr/bin/env python
# Hi, Richie is here,. I am going to make somekind of a login system using#
# python. Any contribution from you would be very appreciate it.

class Passwdlogin(object):
        list = []
        def __signin__(self):
            username = raw_input("Please insert your username now\n")
            password = raw_input("Please insert your password now\n")

        def __signup__(self):
            username = raw_input("Please insert a new username\n")
            password = raw_input("Please insert your password\n")

try:
    signup = input("Are you already signup yet?"
                "\n1. Yes\n2. No\n")
    if signup == 1:
        Passwdlogin().__signin__()
    elif signup == 2:
        Passwdlogin().__signup__()
    else:
        print ("Sorry, no choose have been exist")

except (EOFError,ValueError,EnvironmentError,RuntimeError,NameError):
    print ("Your answer is missmatch")
    pass
