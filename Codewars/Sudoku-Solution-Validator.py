num = [1,2,3,4,5,6,7,8,9]
def validSolution(board):
    lst=[[0]*9 for p in range(9)] #zero list 9x9
    # nbn=[[0]*9 for p in range(9)] #zero list 9x9
    print(lst)
    tf=bool(True)
    tri = 3
    start=0
    for i in range(9):
        for k in range(9):
            lst[i][k] = board[k][i] # pivot list create
    numb=0

    t=[]
    s=[]
    n=[]
    for i in range(9):
        t+=board[i][0:3]
        s+=board[i][3:6]
        n+=board[i][6:9]
        numb+=1
        if numb % 3 == 0 :
            print(t,s,n)

            numb=0
            for c in range(9):
                if t.count(c+1) >= 2 or s.count(c+1) >= 2 or n.count(c+1) >= 2 :
                    return False
            t=[]
            s=[]
            n=[]
            #break
        #print(board[i][3:6])
        #print(board[i][6:9])
    #print(nbn)





    for a in board: # row list check
        for j in num:
            if a.count(j) == 2:
                tf=False
                print("???")
                break
    for b in lst: # col list check
        for l in num:
            if b.count(j) ==2:
                tf=False
                break
    return tf



print(validSolution([\
[5, 3, 4, 6, 7, 8, 9, 1, 2],\
[6, 7, 2, 1, 9, 5, 3, 4, 8],\
[1, 9, 8, 3, 4, 2, 5, 6, 7],\
[8, 5, 9, 7, 6, 1, 4, 2, 3],\
[4, 2, 6, 8, 5, 3, 7, 9, 1],\
[7, 1, 3, 9, 2, 4, 8, 5, 6],\
[9, 6, 1, 5, 3, 7, 2, 8, 4],\
[2, 8, 7, 4, 1, 9, 6, 3, 5],\
[3, 4, 5, 2, 8, 6, 1, 7, 9]]))
