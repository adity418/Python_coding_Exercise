def find_first_occurrence(string):
   
    for char in enumerate(string):
        if char != " ":
            return char
    return -1

# Example usage:
string = "this is my interview"
print("The index of the first occurrence of any character is:", find_first_occurrence(string))