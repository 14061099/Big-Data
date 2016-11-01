#!/usr/bin/env python

import sys
 
# maps words to their counts
word2count = {}#保存单词出现总数的数组
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()#消除行末和行首所有的空格
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)#拆分得到inkey，invalue

    # convert count (currently a string) to int
    try:
        count = int(count)#将invalue变为整型数
        word2count[word] = word2count.get(word, 0) + count #get语句：得到对应键的值，如果键不存在则返回0；累加单词出现总数outvalue
    except ValueError:#抛出异常，并没什么卵用
        # count was not a number, so silently
        # ignore/discard this line
        pass

# write the results to STDOUT (standard output)
for word in word2count:#将
	print '%s\t%s' % (word, word2count[word]) #将数组中的每一项输入到hdfs的文件中，outkey，outvalue
 
