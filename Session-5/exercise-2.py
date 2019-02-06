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

sequence1 = input('Enter the sequence 1:')
s1= count_bases(sequence1)
sequence2 = input('Enter the sequence 2:')
s2 =count_bases(sequence2)

print ('This sequence 1 is {} bases in leght.'.format(len(sequence1)))
for i in s1:
    print ("Base {}".format(i))
    print("   Counter {}".format(s1[i]))
    print("   Porcentage {}".format( round (100.0 * s1[i] / len(sequence1),1)))

print ('This sequence 2 is {} bases in leght.'.format(len(sequence2)))
for i in s2:
    print ("Base {}".format(i))
    print("   Counter {}".format(s2[i]))
    print("   Porcentage {}".format( round (100.0 * s2[i] / len(sequence1),1)))

