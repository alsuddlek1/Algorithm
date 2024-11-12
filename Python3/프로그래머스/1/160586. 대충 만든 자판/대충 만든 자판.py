## targets 을 만들기 위해 keymap 에서 최소한 몇번 누르기

def solution(keymap, targets):
    answer = []
    # 1. targets[i][j] 와 keymap 비교
    for i in range(len(targets)):       
        target_dic = {}
        
        for j in range(len(targets[i])):
            target_dic[targets[i][j], j] = 101
        
            # 1-2. keymap 비교
            for k in range(len(keymap)):
                for l in range(len(keymap[k])):
                    if targets[i][j] == keymap[k][l]:
                        target_dic[targets[i][j], j] = min(target_dic[targets[i][j], j], l+1)
            
        # print(target_dic)
        
        cnt = 0
        for a in target_dic:
            if target_dic[a] == 101:
                cnt = -1
                break
            else:
                cnt += target_dic[a]
        
        answer.append(cnt)

            
        

    
    return answer