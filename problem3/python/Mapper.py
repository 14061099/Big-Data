#!/usr/bin/env python
	
import sys
import json
 
for line in sys.stdin:
	line = line.strip()

	record = json.loads(line)
	key = record[0];
	print '%s\t%s' % (key, 1)


