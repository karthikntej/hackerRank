t = int ((raw_input()).strip())

def fact( n):
	if n == 0:
		return 1

	return n * fact(n-1)

while t > 0:
    
	t-=1
	n = int ((raw_input()).strip())

	ans = fact(n)

	print ans


