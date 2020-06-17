#def stack(priorities, location):

def solution(priorities, location):
    p = priorities
    cnt = 0
    max_i = p.index(max(p))

    if max_i == location: # 제일 큰 숫자가 location(인덱스면) 1순위니까 바로 리턴
        return 1

    while(p):
        if max(p) == p[0] :
            p.pop(0)
            location -=1
            cnt += 1
            if location < 0 :
                return cnt
        else :
            p.append(p.pop(0))
            if location:
                location -=1
            else :
                location = len(p)-1

print(solution([1, 1, 9, 1, 1, 1], 0) )
