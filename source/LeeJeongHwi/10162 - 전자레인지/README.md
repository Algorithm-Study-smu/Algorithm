# 전자레인지
![image-20200914234737911](./problem)

https://www.acmicpc.net/problem/10162

**예제 입력**

`100`

**예제 출력**

`0 1 4`

## 문제 접근 방법
* 알고리즘 분류 : 그리디
A : 5분 / B : 1분 / C : 10초
* **최소 조작 횟수** 를 구하기

A를 300초 , B를 60초 , C를 10초

가장 작은 초(C = 10)로도 정확히 0을 맞출 수 없을 때에는 -1을 출력하므로 10으로 먼저 나눠지는지 확인한다.

1. 그리디로 해결해야하므로 A->B->C 순으로 T초에서 뺀다.
   * T-A < 0 이면 T-B를 수행
     * count+=1 증가
   * T-B < 0 이면 T-C를 수행
     * count+=1 증가
   * 만약 T-C < 0이면 -1을 출력

> 파이썬은 일반적으로 재귀의 속도(함수 호출 속도)가 느리다.
>
> 하지만 재귀 연습겸 재귀로 문제를 해결

### 코드

```python
from sys import stdin
# stdin = open('input.txt','r')

def solution(val,a,b,c):
    if val == 0:
        return (a,b,c)
    if val-300 >= 0:
        return solution(val-300,a+1,b,c)
    elif val-60 >= 0:
        return solution(val-60,a,b+1,c)
    elif val-10 >= 0:
        return solution(val-10,a,b,c+1)

n = int(stdin.readline())
if n%10!=0:
    print(-1)
else:
    print(*solution(n,0,0,0))
```

### Time Complexity

O(N) (보다는 적게 걸린다)

:heavy_check_mark: AC

:alarm_clock: 64ms


### 잘못된 접근 방식

* 굳이 재귀로 해결하지 않아도 단순히 몫,나머지로 충분히 해결가능함 --> 시간 절약...!

  ```python
  n = int(input())
  remain = 0
  if n%10 != 0:
      print(-1)
  else:
      a = n/300
      n = n%300
      b = n/60
      n = n%60
      c = n/10
      print("%d %d %d"%(a,b,c))
  ```

  