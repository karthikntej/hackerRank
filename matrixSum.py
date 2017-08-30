n,m = map(int, raw_input().strip().split())

i = j = 0 
arr = []
while i < n:
	arr.append(map(int,raw_input().split()))
	i+=1

i = 0

while i < n:
	j = 0
	while j < m:
		print arr[i][j],
		j += 1
	i += 1
