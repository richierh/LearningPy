import sys

import time



# Without flushing

print "Without flushing the stdout stream"

for n in range(0,10):

    print "-",

    time.sleep(1.0)
