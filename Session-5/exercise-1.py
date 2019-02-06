def count_bases (seq):
    count_A = 0
    count_C = 0
    count_T = 0
    count_G = 0
    for i in seq:
        if i == 'A':
            count_A = count_A + 1
        elif i == 'C':
            count_C = count_C + 1
        elif i == 'T':
            count_T = count_T + 1
        elif i == 'G':
            count_G = count_G + 1
    dic = {"A": count_A, "C":count_C, "T":count_T, "G": count_G}
    return dic

sequence = input('Enter the sequence:')
s= count_bases(sequence)

print ('This sequence is {} bases in leght.'.format(len(sequence)))
for i in s:
    print ("Base {}".format(i))
    print("   Counter {}".format(s[i]))
    print("   Porcentage {}".format( round (100.0 * s[i] / len(sequence),1)))



