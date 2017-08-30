s = raw_input().strip()

#n = sum(1 for c in s if c.isupper())  #One line code
c = ''
n = 0
for c in s:
#	print c
	if c.isupper():
		n+=1

print n+1
