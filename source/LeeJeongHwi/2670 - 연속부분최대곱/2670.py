from sys import stdin
stdin = open('input.txt','r')

n = int(stdin.readline())
dp = [float(stdin.readline()) for _ in range(n)]

for i in range(1,n):
    dp[i] = max(dp[i],dp[i]*dp[i-1])
print("%.3f"%max(dp))
print(dp)