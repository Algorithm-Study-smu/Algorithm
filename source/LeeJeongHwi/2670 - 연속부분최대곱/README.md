# 연속부분최대곱

https://www.acmicpc.net/problem/2670

## 문제 접근 방법

실질적으로 모든 수를 다 곱하면 0.98x 가 나온다.

완전탐색으로 풀면 10000*10000 = 100000000 이므로 시간초과가 일어난다. 따라서 DP로 풀어야한다.

**연속적**인 것에 초첨을 두어야한다.

```dp[i] = max(dp[i-1]*nlist[i], nlist[i])```

* dp[i-1]*nlist[i]의 값이 nlist[i] 값보다 크면 연속적으로 다음 숫자를 이어가는 것

==> DP내에 가장 큰 값이 답

| 0    | 1    | 2    | 3    | 4     | 5     | 6     | 7    |
| ---- | ---- | ---- | ---- | ----- | ----- | ----- | ---- |
| 1.1  | 0.77 | 1.3  | 1.17 | 1.638 | 1.310 | 0.917 | 1.4  |

### 코드

```python
from sys import stdin
stdin = open('input.txt','r')

n = int(stdin.readline())
dp = [float(stdin.readline()) for _ in range(n)]

for i in range(1,n):
    dp[i] = max(dp[i],dp[i]*dp[i-1])
print("%.3f"%max(dp))
```

* 주의할 점은 round(max(dp),3)을 쓰면 반올림 하므로 틀린답이 나온다.
* %.3f 으로 하면 단순히 자르는 것인지 내림or올림을 하는 것인지 잘 모르겠다.

### Time Complexity

* O(N)



### 잘못된 접근 방식

* 냅색으로 풀려고 했으나 답이 안됨
* 2차원 배열로 풀면 무조건 시간초과

> 해당 문제는 해설을 참조