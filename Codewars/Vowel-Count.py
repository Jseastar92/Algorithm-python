def getCount(inputStr):
    num_vowels = 0
    # your code here
    for i in range(len(inputStr)) :
        if inputStr[i] in'aeiou'  :
            num_vowels += 1
    return num_vowels


print(getCount('aeioqwr'))
