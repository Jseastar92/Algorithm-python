def solution(array, commands):
    ans = [sorted(array[lst[0]-1:lst[1]])[lst[2]-1] for lst in commands]
    return ans

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
