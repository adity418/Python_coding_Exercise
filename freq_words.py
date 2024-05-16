# Count the frequency of words appearing in a string Using Python

class Solution:
    def freq_words(self, str):
        lst = str.split()
        dct = {}

        for i  in lst:
            # if i not in dct.keys:
            #     dct[i] = 0
            dct[i] = dct.get(i, 0) + 1
        print(dct)