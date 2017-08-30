# -*- coding: utf-8 -*-
import math

n,k = map(int, raw_input().split())

x = map(int, raw_input().split())

y = map(int, raw_input().split())

distance = []
for i in range(0,len(x)):
	distance.append(math.sqrt(x[i]**2 + y[i]**2))

distance.sort()

print distance

print int(math.ceil(distance[k-1]))

''' THE END '''

"""
Problem exaplanation
You are given the location of 
N
N
 devices on a coordinate plane and an integer 
K
K
. Location of 
i
t
h
i
t
h
 device is donated by 
(
X
i
,
Y
i
)
(
X
i
,
Y
i
)
. A modem is located at 
(
0
,
0
)
(
0
,
0
)
. The range of modem is circular. All the devices within the range of the modem will connect to the modem. You have to find the minimum integral radius of the circular range of the modem such that at-least 
K
K
 devices will connect to the modem.

Input:
First line contains two integers, 
N
N
 
(
1
≤
N
≤
10
5
)
(
1
≤
N
≤
10
5
)
 and 
K
K
 
(
1
≤
K
≤
N
)
(
1
≤
K
≤
N
)
. Second line contains 
N
N
 space separated integers denoting the array 
X
X
 
(
−
10
9
≤
X
i
≤
10
9
)
(
−
10
9
≤
X
i
≤
10
9
)
. Third line contains 
N
N
 space separated integers denoting the array 
Y
Y
 
(
−
10
9
≤
Y
i
≤
10
9
)
(
−
10
9
≤
Y
i
≤
10
9
)
.

Output:
Print one integer, denoting the minimum integral radius of the circular range of the modem such that at-least 
K
K
 devices will connect to the modem.

SAMPLE INPUT 
3 3
1 -1 1
1 -1 -1
SAMPLE OUTPUT 
2
Explanation
All the devices are at distance 
√
2
2
 from the modem. So, the minimum integral radius of the circular range of the modem such that at-least 
3
3
devices will connect to the modem will be 
2
2
.
"""
