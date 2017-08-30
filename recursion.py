# -*- coding: utf-8 -*-

arr = []

def recursion(n,a):
	arr.append(a)
	a += 1
	n -= 1

	if n > 0:
		recursion(n,a)

recursion(5,0)

print arr,
