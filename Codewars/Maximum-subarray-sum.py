# The maximum sum subarray problem consists in finding the maximum
#sum of a contiguous subsequence in an array or list of integers:
#
# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the
#maximum sum is the sum of the whole array. If the list is made up of
#only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty
#list or array is also a valid sublist/subarray.

def maxSequence(arr):
    #print(max(sum([i for i in range(len(arr))] )))
    summ=0
    for i in range(len(arr)):
        a = sum(arr[i::])
        for s in range(len(arr)):
           c = sum(arr[i:s:])
           if c >= summ :
               summ = c
        if a >= summ :
            summ = a
        print('summ:', summ)
    print()
    return summ
	# ...

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# # best  문제 접근 방식/ 창의성 / 수학적사고
# def maxSequence(arr):
#     max,curr=0,0
#     for x in arr:
#         curr+=x
#         if curr<0:curr=0
#         if curr>max:max=curr
#     return max
