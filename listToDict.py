# Conversion of two list into Dictionary Using Python
class Solution:
    def list_to_dict(self, lst1, lst2):
        dct = dict(zip(lst1,lst2))
        print(dct)

    def dict_to_tuple(self, dct):
        for i in dct.items():
            print(i)