# Binary Search (recursive)
# elements : target, data(ASC), start, end, mid
# if Sorted data, O(log N)

def binary_search(target, data, start, end):
    if start > end :
        return None

    mid = (start+end) // 2

    if target == data[mid]:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else :
        end = mid - 1

    return binary_search(target, data, start, end)


data = [i*3 for i in range(900)]
start=0
end=len(data)-1
print(binary_search(150, data, start, end))
