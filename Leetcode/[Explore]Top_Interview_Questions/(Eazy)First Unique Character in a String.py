
'''
Memory Distribution 99.77% !!
but runtime....
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,v in enumerate(s[:]):
            if s[:].count(v) == 1:
                return i
        return -1

'''
second solution!
52% runtime
97.44% memory
'''
    def firstUniqChar(self, s: str) -> int:
        repeat_list = []
        last_ind = len(s)
        for i,v in enumerate(s[:]):
            
            if i == last_ind:
                if v in repeat_list:
                    return -1
                else:
                    return i
            
            if v in repeat_list:
                continue
                
            if v in s[i+1:]:
                repeat_list.append(v)
            else:
                if v not in repeat_list:
                    return i
            
        return -1


'''
56ms 99% runtime solution(다른사람)
컬렉션 Counter을 썼다.
TODO : 컬렉션 공부하기!
'''
    def firstUniqChar(self, s: str) -> int:
            counter = Counter(s)
            for i in counter:
                if counter[i] == 1:
                    return s.index(i)
            return -1