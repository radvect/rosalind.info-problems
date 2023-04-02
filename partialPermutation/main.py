n, k=map(int,input().split())

p = 1
for i in range(k):
    p = p*(n-i)

p = p%1000000

print(p)