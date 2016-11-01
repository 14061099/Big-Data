#!/usr/bin/env python

import sys
 
ship = {}
 
for line in sys.stdin:
    line = line.strip()
 
    name1, name2 = line.split('\t', 1)
    if name1 not in ship:
        ship[name1]=[]
    if name2 not in ship[name1]:
        ship[name1].append(name2)
    if name2 not in ship:
        ship[name2]=[]
    if name1 not in ship[name2]:
        ship[name2].append(name1)

# write the results to STDOUT (standard output)
for name in ship:
    for friend in ship[name]:
        print '["%s","%s"]' % (name, friend) 
 
