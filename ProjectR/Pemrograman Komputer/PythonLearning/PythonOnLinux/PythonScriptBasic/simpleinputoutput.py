# usr/bin/python #
"This is my first python script and"
" I just want to make the basic script"

print ("Hello World,\n    I am a beginner using Python Programming Language"
       "\nFirst time I look it , and I just love it")
print ("\nThis is my first Python Language using IDLE")

d = raw_input("What is your name anyway?\n")

print ("Hi ,"+d+"\nI hope you can enjoy this simple apps")
print ("Now we are going to count the first 15"
       "numbers from the value you typed")
fn = input("Please input your value (don't put a string okay)")
for i in xrange(fn,fn+15):
 fn = fn+1
 print ("%d\n")%fn
