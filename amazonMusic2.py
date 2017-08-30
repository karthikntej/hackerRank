sum = 0

def recursion(num, j):
	sum = 0
#	print "recursion ",num, j
	ncj = num - coins[j]

	if (ncj == 0):
		return 1

	if (ncj < 0):
		return 0

	sum += recursion(ncj,j)

	while(j+1 < len(coins)):
		j += 1
		sum += recursion(ncj, j)

#	print "(",num,sum,")"
	return sum


n = int (raw_input().strip())

coins = map(int, raw_input().strip().split())

i = 0

while (i < len(coins)):
	sum += recursion(n,i)
	i += 1
print sum
