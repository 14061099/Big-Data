#!/usr/bin/env python

import sys
 
friendcount = {}
 
for line in sys.stdin:
    line = line.strip()

    name, count = line.split('\t', 1)

    try:
        count = int(count)
        friendcount[name] = friendcount.get(name, 0) + count
    except ValueError:
        pass

for name in friendcount:
	print '["%s",%s]' % (name, friendcount[name]) 
 
