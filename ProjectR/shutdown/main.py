from inputsys import *
import subprocess
global answer


j = "no%d"%int(answer)
print eval(j)
print j

if eval(j) == no2:
	subprocess.call(["ssh ","%s"%eval(j)])
	print "oke"
	

else :
	print "nggak oke"

#subprocess.Popen("ssh "
