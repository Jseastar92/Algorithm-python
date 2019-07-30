def find_even_index(arr):
    #your code here
    if arr.count(0)==len(arr) :
        return "Should pick the first index if more cases are valid"
    a = [ i for i in range( len(arr) ) if sum(arr[i::1]) == (sum(arr[i::-1])) ]

    if not a : return -1
    else : return a

print(find_even_index([0,0,0,0,0]))
