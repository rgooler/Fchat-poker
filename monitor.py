#!/usr/bin/python

from datetime import datetime,timedelta
import sys

import subprocess
import os

def tail( f, window=20 ):
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if (bytes - BUFSIZ > 0):
            # Seek back one whole BUFSIZ
            f.seek(block*BUFSIZ, 2)
            # read BUFFER
            data.append(f.read(BUFSIZ))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            data.append(f.read(bytes))
        linesFound = data[-1].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return '\n'.join(''.join(data).splitlines()[-window:])


def get_last_time():
    fh = open('Pokerbot.log','r')
    lastline = tail(fh,1)
    fmat='%Y-%m-%dT%H:%M:%S'
    #2012-04-22T01:44:12
    last_time = datetime.strptime(lastline[0:19],fmat)
    return last_time
    
if __name__ == "__main__":
    last_time  = get_last_time()
    cur_time   = datetime.now()
    is_bad =  (cur_time - last_time) > timedelta(seconds=2)

    if is_bad:
        sys.exit(0)
    else:
        sys.exit(1)
#        try:
#            pidfile = 'pokerbot.pid'
#            fh = open(pidfile)
#            pid = fh.read()
#            fh.close()
#            print "PID: ", pid
#            subprocess.call("/bin/kill -9 %s" % pid)
#        except:
#            pass
#
#        try:    subprocess.call("/bin/rm pokerbot.pid")
#        except: pass
#
#        try:    subprocess.call('./Pokerbot.py')
#        except: pass

