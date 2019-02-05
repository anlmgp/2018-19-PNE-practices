def count_a(seq):
    """Calculating the number of As in the sequence"""

    #Counter for the As
    result = 0

    for b in seq:
        if b == 'A':
            result += 1

    #Return the result
    return result


#Main program
s = 'AGTACACTGGT'
na = count_a (s)
print("The number of As is: {}" .format(na))

#Calculate the total sequence lenght
tl = len (s)

