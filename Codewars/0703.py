# 맨 뒷자리 두개 변경 -> 아니다? 그럼 맨뒤에서2번째 자리 두개 변경 이런식으로 1까지 만약에 크다 되면 바로 끝

def next_bigger(n):
    changed=0
    a=list(str(n))
    for i in range(len(a),0,-1):
        if (i-2) == -1:
            break
        if a[i-1] > a[i-2] :
            a[i-1] , a[i-2] = a[i-2],a[i-1]
            changed+=1
            break
    #your code here
    b = ''.join(i for i in a)
    b = int(b)

    return b if changed>=1 else -1

print(next_bigger(144))#143
