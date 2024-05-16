# Find out common letters between two strings Using Python

class Solution:
    def common_letter(self, str1, str2):
        s1 = set(str1)
        s2 = set(str2)
        lst = s1 & s2
        return lst

sol = Solution()
str1 = 'avinash'
str2 = 'aditya'
print(sol.common_letter(str1, str2))