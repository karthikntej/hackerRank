#!/bin/python

def printFun(s,n):
	i = 0
	while(i < n):
		i += 1
		print s

def nextMove(n,r,c,grid):
	pc = pr = 0
	i = 0
	while(i<n):
		if('p' in grid[i]):
			pr = i
			pc = grid[i].index('p')
			break
		i+=1

	dif = 0
	
	dif = r - pr
	if dif > 0:
		printFun("UP",dif)
	else:
		printFun("DOWN",-dif)

	dif = c - pc
	if dif > 0:
		printFun("LEFT",dif)
	else:
		printFun("RIGHT",-dif)
	
	return ""
	



n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)


