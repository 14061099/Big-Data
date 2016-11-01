#!/usr/bin/env python
	
import sys
import json

key={}
 
for line in sys.stdin:
	line = line.strip()
	record = json.loads(line)
	text = line
	Type = record[0];
	value = record[1];
        if Type=="order":
		key[value]=line
	if Type=="line_item":
		print '%s\t%s' % (key[value],text)



