# implement variable length argument

def average(*t):
    avg = sum(t)/len(t)
    print("Average is",avg)
average()