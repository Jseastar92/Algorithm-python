def find_even_index(arr):

    f = [ i for i in range( len(arr) ) if sum(arr[i::1]) == (sum(arr[i::-1])) ]
    return f[0] if f else -1
    #if not f : return -1
    #else : return f[0]

print(find_even_index([50,-50,50,-50,50]))
