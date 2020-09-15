a = int(input())

time = [300, 60, 10]
count = [0, 0, 0]
i = 0
for i in range(3):

    while(a >= time[i]):
        a = a - time[i]
        count[i] = count[i]+1

if a != 0:
    print("-1")
else:
    for i in range(3):
        print(count[i], end=' ')
