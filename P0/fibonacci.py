def fibonacci (n):
    a = 1
    b = 0
    for i in range(n):
        a,b = b, a + b
    return a

n = int(input('Select the number of the sequence:'))
print ('The number of the postion',n,'of the fibonnaci serie is',fibonacci(n))