#  FIND MISSING NUMBER IN AN ARRAY

# class Solution:
#     def missing_num(arr):
#        n = len(arr)+1
#        sum1 = 0
#        total = n*(n-1)//2
#        sum1 = sum(arr)
#        return (total-sum1 )
    
# #  XOR method
#     def num_missing(arr):
#         n = len(arr)
#         xor_a = arr[0]
#         for index in range(1,n):
#             xor_a = xor_a^arr[index]
#         x2 = 0
#         for index in range(1, n+2):
#             x2 = x2^index
#         return (xor_a^x2)


def findMissingNumbers(n):
    numbers = set(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    

n = [1,2,3,5,6,7,8,9,10,11,13,14,16]
print(findMissingNumbers(n))
