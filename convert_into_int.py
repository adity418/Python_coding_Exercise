def convert_to_integer(string_list):
    """
    Convert a list of strings representing digits into integers without using int() method.

    Args:
    - string_list (list): List of strings representing digits.

    Returns:
    - list: List of integers.
    """
    integer_list = []
    for digit_str in string_list:
        digit_int = 0
        for char in digit_str:
            digit_int = digit_int * 10 + (ord(char) - ord('0'))
        integer_list.append(digit_int)
    return integer_list

# Example usage:
string_list = ['1', '2', '3', '4', '5']
integer_list = convert_to_integer(string_list)
print("Converted integers:", integer_list)
