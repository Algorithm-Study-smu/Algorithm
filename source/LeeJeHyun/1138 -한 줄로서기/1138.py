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
