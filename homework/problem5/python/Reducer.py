#!/usr/bin/env python

import sys
 
group=[]
 
for line in sys.stdin:
    line = line.strip()
 
    id,s = line.split('\t', 1)

    if s not in group:
        group.append(s)

for s in group:
	print '"%s"' % (s) 
 
