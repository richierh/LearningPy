import sys

import time


print "With flushing"
for n in range(0,10):

    print "-",

    sys.stdout.flush()

    time.sleep(1.0)
