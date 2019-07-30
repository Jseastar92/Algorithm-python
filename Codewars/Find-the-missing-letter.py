#by sst

def find_missing_letter(chars):
    i = ord(chars[0])
    for c in chars:
        if ord(c) == i : None
        else :
            temp=chr(i)
            i += 1
        i += 1
    return temp

print(find_missing_letter(['a','b','c','d','f']))

# chr = Ascii number to Char
# ord = char to ascii number
    #if you want to print more than 2 words, temp=list()
    # and to if sequence, add else : temp.append(chr(ind))
