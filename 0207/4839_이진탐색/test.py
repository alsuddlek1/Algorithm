import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def page_finding_count(page, goal):
    start = 1
    end = page
    cnt = 1
    while start <= end:
        mid = int((start + end)/2)
        if goal == mid:
            return cnt
        elif goal < mid:
            end = mid - 1
            cnt += 1
        elif goal > mid:
            start = mid + 1
            cnt += 1

for test_case in range(1, T + 1):
    page, a_goal, b_goal = map(int, input().split())
    if page_finding_count(page, a_goal) > page_finding_count(page, b_goal):
        print(f'#{test_case} B')
    elif page_finding_count(page, a_goal) == page_finding_count(page, b_goal):
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} A')