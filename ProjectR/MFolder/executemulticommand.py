# -*- coding: utf-8 -*-
import subprocess
import os


def execution():
    Documents = "Downloads"
    home = "cd /home/pmc/" + Documents + " && "
    command = home + "ls"
    print (command)
    #print os.path.dirname(home)
    result = subprocess.Popen(command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True)
    for line in result.stdout.read().split():
        if line == "anjali.odt":
            print "ini ada loh yang namanya anjali"
        else:
            print line


def removeff():
    pass

execution()