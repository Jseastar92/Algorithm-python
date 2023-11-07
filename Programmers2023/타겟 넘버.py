def solution(numbers, target):
    def dfs(numbers, acc, index, target):
        print(len(numbers) <= index, len(numbers), index)
        if len(numbers) < index and acc==target :
            return 1
        
        if len(numbers) < index :
            return 0
        
        peekNum = numbers[index]
        cnt = 0
        cnt += dfs(numbers, acc+peekNum, index+1, target)
        cnt += dfs(numbers, acc-peekNum, index+1, target)
        return cnt
    
    answer = dfs(numbers, 0, 0, target)    
    return answer

solution([4,1,2,1], 4)