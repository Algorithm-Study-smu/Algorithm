# 연속부분최대곱

https://www.acmicpc.net/problem/2670

## 문제 접근 방법

1차원 배열에 수들을 추가한뒤 연속된 수들의 곱중에 최고값을 찾는것이기 때문에 
계속 곱한값에 다음것을 곱했을때 그전 값보다 더 크다면 dp 에 추가하면된다.
결과적으로 dp list에 가장큰값이 가장큰 값 


==> DP내에 가장 큰 값이 답

| 0    | 1    | 2    | 3    | 4     | 5     | 6     | 7    |
| ---- | ---- | ---- | ---- | ----- | ----- | ----- | ---- |
| 1.1  | 0.77 | 1.3  | 1.17 | 1.638 | 1.310 | 0.917 | 1.4  |
정휘가 만든 표 가지고옴 호호
### 코드

```python
a = int(input())
dp= []
result =0

for i in range(a):
    dp.append(float(input()))

for j in range(1,a):
    dp[j] = max((dp[j]), (dp[j]*dp[j-1]))
    result = max(result, dp[j])

print("%.3f" %result)
```


### Time Complexity

* O(N)

### 잘못된 접근 방식

처음에는 입력 list 와 dp list 따로 만들었지만 
그럴 필요가 없다!

파이썬엔 double이 없다는것을 기억하자! 
