!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append(Jala);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
Jala = 3,4,5,6; 
mylist = [10,20,30,"hello"];
changeme( mylist );
print "Values outside the function: ", mylist


#!/usr/bin/python


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme ("I'm first call to user defined function!")
printme ("Again second call to the same function")
