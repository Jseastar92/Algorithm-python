# Random Weighted Choice Fucntion,
# Quick
# 정수시퀀스의 각 값은 어떤 값에 대한 가중치이다
import random

def quick(arr,rnd):

    if len(arr) <= 1:
        return arr

    mid = arr[ len(arr) // 2 ]
    print(mid, rnd, arr,len(arr)//2 )
    if rnd < mid :
        print("mid is big!")
        return quick( arr[0:(len(arr)//2)], rnd)
    elif rnd > mid :
        print("mid is small!")
        return quick( arr[(len(arr)//2):-1], rnd)
    else :
        print("eqaul")
        return mid
    return arr




def choice(weights):
    #weight = []
    max = weights[-1]

    rnd = round(random.random() * max) #  weighted random 생성
    print(quick(weights,int(rnd)))

    # for i, w in enumerate(weight): # 가중치에 대한 랜덤 값 보다 큰 인덱스를 찾아 Return
    #     if rnd < w:
    #         return i

print(choice([100, 150, 180 , 200]))
