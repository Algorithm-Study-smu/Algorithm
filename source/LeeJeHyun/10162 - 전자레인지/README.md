# 전자레인지 문제

https://www.acmicpc.net/problem/10162

## 문제 접근 방법

3개의 시간조절용 버튼이있기 때문에 큰것부터 이용해 시간을 줄여나가면된다.
버튼은 각각 5분 1분 10초 이기 때문에 초반위로 일정하게 배열을 만들어 준다.

time [300,60,10] 그러고 입력받은 초가 time의 최소인 10보다 작거나 같을때까지
빼준다. 그리디 알고리즘을 사용하기 때문에 값이 큰 거부터 빼준다.
그리고 새로운 배열에 time이 쓰인걸 기록한다.

### 코드

```python
a = int(input())

time = [300, 60, 10]
count = [0, 0, 0]
i = 0
for i in range(3):  ##time길이 만큼

    while(a >= time[i]):
        a = a - time[i]
        count[i] = count[i]+1

if a != 0:  ##안나누어 떨어질때
    print("-1")
else:
    for i in range(3):
        print(count[i], end=' ')

```

### Time Complexity

정확히 모르겠다.

### 잘못된 접근 방식

시간이 74초나 걸렸다 더 짧게 할수는 없을까..?
