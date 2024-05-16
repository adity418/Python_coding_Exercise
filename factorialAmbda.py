# Factorial using lambda function

f = lambda n: 1 if n==0 else n*f(n-1)
print(f(5))