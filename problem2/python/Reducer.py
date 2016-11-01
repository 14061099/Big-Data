#!/usr/bin/env python

import sys
 
 
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)

    print '%s,%s' %(key,value) 

 
