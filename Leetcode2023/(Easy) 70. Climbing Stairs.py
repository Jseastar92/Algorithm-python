class Solution:
    def climbStairs(self, n: int) -> int:
        def recur(n, sum) -> int:
            if sum > n :
                return 0
        
            if sum == n :
                return 1

            result = 0
            result += recur(n, sum+1)
            result += recur(n, sum+2)
            return result
        return recur(n, 0)
    
Solution.climbStairs(Solution,3)

# 1, 2로 더해서 n까지 나오는 경우의 수 구하는 문제.
# 1 <= n <= 45
# 위 코드는 n=38일 때 Time Exceeded .
# 그럼 어떻게 시간을 줄일 수 있을까


# 피보나치로 푸는거였다.