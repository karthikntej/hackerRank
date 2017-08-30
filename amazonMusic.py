

def recursion(num,j,sum):
	if (num - coins[j] == 0):
		return 1

	elif (num - coins[j] > 0):
		sum = recursion(num-coins[j], j, 0)

	else:
		return 0

	while j+1 < len(coins):
		sum += recursion(num, j+1, 0)
		j+=1
		print "j ->",j

	print "(",num,sum,")"
	return sum


n = int (raw_input().strip())

coins = map(int, raw_input().strip().split())

print "\n"
print recursion(n,0,0)
