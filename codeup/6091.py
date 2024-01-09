a,b,c = map(int, input().split())

# 최소 공배수 이용하기
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)