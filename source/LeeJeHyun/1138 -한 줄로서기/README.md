# 한 줄로서기 문제

https://www.acmicpc.net/problem/1138

## 문제 접근 방법

리스트에 키가 1인 순서대로 자기보다 키가 작은 사람의 수를 알려준다. 키가1인사람은
무조건 다른 사람보다 키가 작기 때문에 입력받은 값이 자기 위치이다.
그다음 입력값들은 자기앞에 0으로 채워넣은 리스트에서 0의 개수를 비우고 채워주면 된다.

### 코드

```python
n = int(input())

a = list(map(int, input().split()))
result = [0]*n

for i in range(n):
    count = 0

    for j in range(n):
        if count == a[i] and result[j] == 0:
            result[j] = i+1
            break
        elif(result[j] == 0):
            count += 1
print(*result)


```

### Time Complexity

O(n^2)

### 잘못된 접근 방식

    for i in range(3):
        print(count[i], end=' ')
    처럼 print 안하고 list 는 그냥 print(*list) 하면 출력이 한칸씩 띄어서 된다
