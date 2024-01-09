a,r,n = map(int,input().split())
result = a

for i in range(n-1):
    result = result * r

print(result)