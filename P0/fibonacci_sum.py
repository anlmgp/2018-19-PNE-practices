def fibonacci (n):
    a = 1
    b = 0
    for i in range(n):
        a,b = b, a + b
    return a

n = int(input('Select the number of the sequence:'))
print (fibonacci(n))