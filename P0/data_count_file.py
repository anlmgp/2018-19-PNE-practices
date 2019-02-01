sequence = open('dna.txt', 'r')
dna = sequence.read()
dna = dna.replace('\n', '')
print( 'The sequence of dna is:', dna)

count_A = 0
count_C = 0
count_T = 0
count_G = 0

print ('The total lengh:', len (dna))
for i in dna:
    if i == 'A':
        count_A = count_A + 1
    elif i == 'C':
        count_C = count_C + 1
    elif i == 'T':
        count_T = count_T + 1
    elif i == 'G':
        count_G = count_G +1

print ('A:', count_A)
print ('C:', count_C)
print ('T:', count_T)
print ('G:', count_G)