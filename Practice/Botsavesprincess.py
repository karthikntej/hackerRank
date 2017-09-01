#!/bin/python

def printFun(str,n):
	i = 0
	while(i<n):
		print "%s"%(str)
		i += 1

def displayPathtoPrincess(n,grid):
	r = 0
	c = 0


	if 'p' in grid[0]:
		n = int(n/2)
		printFun('UP',n)
		c = grid[0].index('p')
		if c == 0:
			printFun('LEFT',n)
		else:
			printFun('RIGHT',n)

	else:
		printFun('DOWN',n/2)
		c = grid[n-1].index('p')
		n = int(n/2)
		if c == 0:
			printFun('LEFT',n)
		else:
			printFun('RIGHT',n)

	


	
 
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)


