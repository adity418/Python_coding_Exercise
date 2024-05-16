#  Two Sum

class Solution:
    def twosum(arr, sum):
        arr.sort()
        left = 0
        right = len(arr) - 1
        while(left<=right):
            if(arr[left]+arr[right]>sum):
                right = right - 1
            elif(arr[left]+arr[right]<sum):
                left = left + 1
            elif(arr[left]+arr[right]==sum):
                print(arr[left], arr[right])
                right = right - 1
                left = left + 1
