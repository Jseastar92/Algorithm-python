# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

# The Hashtag Generator
def generate_hashtag(s):
    sre = s.title().replace(' ','')
    print(sre)
    #return '#'+''.join(i.capitalize() for i in s.split())
        #i.capitalize()
    #.capitalize()
    #your code here

print(generate_hashtag('codewars is nice'))


# best case, 이거 마지막 리턴 조건문 방식 참고!
# def generate_hashtag(s):
#     ans = '#'+ str(s.title().replace(' ',''))
#     return s and not len(ans)>140 and ans or False
