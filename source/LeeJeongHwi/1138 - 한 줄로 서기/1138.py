from sys import stdin
from collections import deque
stdin = open('input.txt','r')

n = int(stdin.readline())
talls = list(map(int,stdin.readline().split()))
ans = deque()
lenCheck = 0
for i,tallPerson in enumerate(talls[::-1]):
    tall = n-i
    if i == 0: #
        lenCheck+=1
        ans.appendleft(tall)
        continue
    count = 0
    for j in range(lenCheck+1):
        if tallPerson > count:
            count+=1
            continue
        elif tallPerson == count:
            ans.insert(j,tall)
            lenCheck+=1
            break
print(*ans)