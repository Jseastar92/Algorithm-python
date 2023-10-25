def solution(n, lost, reserve):
    only_lost = [l for l in lost if not l in reserve]
    only_reserve = [l for l in reserve if not l in lost]
    
    only_lost.sort()
    only_reserve.sort()
    for i in only_reserve:
        if i-1 in only_lost:
            only_lost.remove(i-1)
        elif i+1 in only_lost :
            only_lost.remove(i+1)
    print(only_lost)
    return n - len(only_lost)
