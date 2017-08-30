sum = 0

def recursion(num, j):
	sum = 0
	print "recursion ",num, j
	ncj = num - coins[j]


	if (ncj == 0):
		return 1

	if (ncj < 0):
		return 0

	sum += recursion(ncj,j)

	
	while(j+1 < leng):
		j += 1
		a= recursion(ncj, j)
		sum += a
		if(a == 0):
			j = leng
	print "(",num,sum,")"
	return sum


n = int (raw_input().strip())

coins = map(int, raw_input().strip().split())
coins.sort()
i = 0
leng = len(coins)
while (i < leng):
	sum += recursion(n,i)
	i += 1
print sum
