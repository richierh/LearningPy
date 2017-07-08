#!/usr/bin/env python
# All SSH libraries for Python are junk (2011-10-13).
# Too low-level (libssh2), too buggy (paramiko), too complicated
# (both), too poor i1 features (no use of the agent, for instance)

# Here is the right solution today:
import subprocess
import sys
from inputsys import myfungsi,klien

HOST=klien
#Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="echo pmc | sudo -S ls"
#shutdown -P now"
#shutdown -P now"

ssh = subprocess.Popen(["ssh","-t","-t","%s" %HOST,COMMAND],
                       shell=False,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()

if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
    
raw_input("Tekan 'Enter' untuk keluar ;)")


