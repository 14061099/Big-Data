#!/usr/bin/env python

import sys
 
# maps words to their counts
idList={} 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, name = line.split('\t', 1)
    if word not in idList.keys():
  	  idList[word]=[]
	  idList[word].append(name)
    else:
          if name not in idList[word]:
	  	idList[word].append(name)
# write the results to STDOUT (standard output)
for key in idList:
    print '["%s",%s]' %(key,idList[key])
 
