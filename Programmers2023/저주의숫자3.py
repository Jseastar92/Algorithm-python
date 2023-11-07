# 저주의 숫자 3

def solution(n):
    answer=0   
    decimal = list()
    get3x(decimal, 1, n)
    return decimal[-1]

def get3x(result, num, n):
    if n == 0: return result
    while True:
        if num%3 == 0 :
            num+=1
            continue
        if str(num).find("3") != -1:
            num+=1
            continue
        break
    result.append(num)
    result = get3x(result, num+1, n-1)
    
    
# 두번째 풀이
def solution(n):
    answer=0
    for i in range(0,n):
        answer+=1
        while answer%3 == 0 or "3" in str(answer):
            answer+=1
    return answer