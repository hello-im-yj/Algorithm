def solution(lottery):
    answer = []
    lottery = sorted(lottery, key=lambda lottery: lottery[0])
    # print(lottery)
    uid = lottery[0][0]
    start_id = 0
    stored = False

    for i in range(len(lottery)) : 
        user_id, result = lottery[i][0], lottery[i][1]

        if stored and user_id != uid : #새로운 id 가 나오면
            start_id = i
            uid = user_id
            stored = False

        if result and not stored : #당첨됨
            answer.append(i-start_id+1)
            stored = True                

    print(answer)
    if len(answer) == 0 : return 0
    else : avg = int(sum(answer)/len(answer))
    return avg