#!/bin/python

import sys

def super_reduced_string(s):

	flag = 1
	s = list(s)
#	print "s is ",s
	while flag == 1:
		i = 1
		l = len(s)

		if l == 1:
			i = l+1	#need to break next loop
		flag = 0
		while i < l:
			if s[i] == s[i-1]:
				del(s[i])
				del(s[i-1])
				flag = 1
				i -= 1
				l -= 2
			i+=1

	s = "".join(s)

	if len(s) == 0:
		s = "Empty String"
	return s

s = raw_input().strip()
result = super_reduced_string(s)
print(result)

