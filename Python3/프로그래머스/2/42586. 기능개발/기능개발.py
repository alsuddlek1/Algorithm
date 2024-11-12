def solution(progresses, speeds):
    answer = []
    
    # 1. 작업 소요 시간
    time_list = [0] * len(progresses)
    
    for i in range(len(progresses)):
        time = 0
        progress = 100 - progresses[i]
        
        if progress % speeds[i] == 0:
            time = progress // speeds[i]
        else:
            time = progress // speeds[i] +1
        
        time_list[i] = time
    
    print(time_list)
    
    # 2. 배포 가능 날짜
    day_list = [1] * len(time_list)
    # day_list[0] = 1
    for i in range(len(time_list)-1):
        for j in range(i+1, len(time_list)):
            if time_list[i] >= time_list[j] and time_list[i] != 0:
                day_list[i] += 1
                time_list[j] = 0
                day_list[j] = 0
            else:
                break
                
    # 3. answer 구하기
    for i in day_list:
        if i != 0:
            answer.append(i)
    
    return answer