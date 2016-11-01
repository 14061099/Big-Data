#!/usr/bin/env python

import sys
 
a = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
b = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
out = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
 
for line in sys.stdin:
    line = line.strip()
 
    type,i,j,value = line.split('\t')
    value=int(value)
    i=int(i)
    j=int(j)
    if type=="a":
	a[i][j]=value
    else:
        b[i][j]=value

for i in range(len(a)):
    for j in range(len(a[0])):
	for k in range(5):
            out[i][j]+=a[i][k]*b[j][k]

for i in range(len(out)):
    for j in range(len(out[0])):
    	print '[%s, %s, %s]' % (i,j,out[i][j]) 
 
