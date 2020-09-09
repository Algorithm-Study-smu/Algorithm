# 연속 부분 최대 곱 -3-

a = int(input())
dp= []
result =0

for i in range(a):
    dp.append(float(input()))

for j in range(1,a):
    dp[j] = max((dp[j]), (dp[j]*dp[j-1]))
    result = max(result, dp[j])
print(dp)
print("%.3f" %result)

