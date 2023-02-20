import sys
sys.stdin = open('sample_input.txt')

from collections import deque

# 맨 앞의 숫자를 맨 뒤로 보내는걸 m번 해야함
# 그랬을때, 맨 앞에 있는 숫자가 뭔지 출력

# 1. arr을 만든다.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

# 2. 맨 앞(왼쪽) 의 숫자를 맨 뒤로 보내야함
# deque를 배웠으므로 이용
    a = deque(arr) # deque
    # print(a) # deque([5527, 731, 31274])

# 3. 리스트에서 쓰는 메서드들을 끝에서만 넣고 빼는게 아니라 왼쪽에서도 뺄수 있네..
     #print(a.popleft())   # 5527, 18140, 17236
# 4.  M번 반복
    for i in range(M):
        a.append(a.popleft())
    print(a)

# 5. 맨 앞 숫자 출력
    result = a[0]
    print(f'#{tc} {result}')
