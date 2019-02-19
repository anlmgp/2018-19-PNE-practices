def fibonacci (n):
    a = 0
    b = 1
    counter = 0
    for i in range(n):
        counter = counter + a
        a,b = b, a + b
    return counter

n = int(input('Select the number of the sequence:'))
print ('The sum of the first',n,'numbers in the fibonnaci serie is',fibonacci(n))