# Largest Number



def largest_number(s, d):
    if s == 0:
        return 0
    if s > 9 * d:
        return -1
    result = ''
    for i in range(d):
        if s >= 9:
            result += '9'
            s -= 9
        else:
            result += str(s)
            s = 0
        if s == 0 and i < d-1:
            result += '0' * (d-i-1)
            break
    return int(result)

print(largest_number(20, 5))

