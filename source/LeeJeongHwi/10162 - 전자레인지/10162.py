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