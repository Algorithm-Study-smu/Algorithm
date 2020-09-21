# 강의실 배정 문제

https://www.acmicpc.net/problem/11000

## 문제 접근 방법

뭔가 이해는 됬지만 어떤 로직을 이용해야 할지를 몰랐다! ㅠㅠ
그리디로 최소 강의실 사용을 위해서라면 강의를 빨리 시작하는 순서대로 정렬해야된다.

우선순위 큐를 이용한다고 한다.
가장 빨리 끝나는 강의시간을 처음에 넣는다.
우선순위 큐의 top은 강의가 가장 빨리 끝나는 강의의 시간이다.
top과 비교했을떄 강의 시작시간이 같거나 더 늦으면 강의실을 쭉 쓸수있다.
top과 비교했을때 강의 시작시간이 더 빠르면 새로운 강의실을 써야되기 때문에 push한다.
그러하면 마지막에는 강의실의 갯수가 들어간다.

### 코드

```python
from queue import PriorityQueue


def work():
    pque = PriorityQueue()

    pque.put((-arr[0][1], arr[0][1]))

    for i in range(1, N):
        if pque.queue[-1][1] <= arr[i][0]:
            pque.get()
            pque.put((-arr[i][1], arr[i][1]))
        else:
            pque.put((-arr[i][1], arr[i][1]))

    print(pque.qsize())
    return


N = int(input())
arr = []
for _ in range(N):
    A, B = list(map(int, input().split()))

    arr.append([A, B])

arr.sort(key=lambda x: x[0])
work()

```

### Time Complexity

O(nlogn)

### 잘못된 접근 방식

제한시간이 1초뿐인 문제이다. 시간복잡도가 매우 낮은 방법을 이용해야된다.
고민해보다가 아예 풀지를 못했다!
우선순위 큐를 쓸생각을 전혀하지 못했다! 자료구조 부분을 더 생각해보자 ㅠ

나중에 꼭 다시 풀어보자
