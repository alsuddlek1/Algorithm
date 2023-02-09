import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()   #패턴
    target = input()    # 전체 텍스트

    # 조사하려고 하는 두 대상의 조사 대상을 내가 직접 컨트롤 하는
    # 인덱스로 조절하면서 비교
    p_idx = 0
    t_idx = 0
    # 최종 결과값
    count = 0       # 패턴의 문장에서 몇번 나오는지 세려고
                    # 조사를 할건데 언제까지 순회
    while t_idx < len(target):
        # 두 값이 같으면 idx를 증가
        if target[t_idx] == pattern[p_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1
        # # 모든 패턴에 대해서 조사를 마쳤다면


        # if target[t_idx] != pattern[p_idx]:
        #     t_idx = t_idx - p_idx
        #     # t_idx += 1
        #     p_idx = -1
        # # 모든 상황에 대해서 항상 증가할 것이기 때문에
        # p_idx += 1
        # t_idx += 1

        if p_idx == len(pattern):
            return t_idx - len(pattern)
        else:
            return -1


    print(f'#{tc} {count}')

