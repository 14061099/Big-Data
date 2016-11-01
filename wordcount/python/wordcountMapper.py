#!/usr/bin/env python
	
import sys
import json
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()#消除行末和行首所有的空格

	# parse the line with json method
	record = json.loads(line)#将第一个语句生成字典，存放于record
	key = record[0];#键是字典的第一项，inkey
	value = record[1];#值时字典的第二项，invalue

    # split the line into words
	words = value.split()#将value以空格分割，outkey

    # increase counters
	for word in words:#遍历所有的词输出
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
		print '%s\t%s' % (word, 1)#outkey，outvalue


