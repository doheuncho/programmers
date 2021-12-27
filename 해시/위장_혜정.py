def solution(clothes):
    clothes_dir = {}
    for i in clothes:
        if i[1] not in clothes_dir :
            clothes_dir[i[1]]= 1
        else :
            clothes_dir[i[1]] +=1
        
    answer = 1
    for i in clothes_dir.values():
        answer *= (i+1)
    return answer - 1