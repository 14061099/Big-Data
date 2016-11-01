#!/usr/bin/env python
	
import sys
import json
 
for line in sys.stdin:
	line = line.strip()

	record = json.loads(line)
	id = record[0];
	i = record[1];
	j = record[2]
	value = record[3];
	if id == "a":
		outkey = '%s\t%s\t%s' %(id,i,j)
	else:
		outkey = '%s\t%s\t%s' %(id,j,i)
	print '%s\t%s' %(outkey,value)


