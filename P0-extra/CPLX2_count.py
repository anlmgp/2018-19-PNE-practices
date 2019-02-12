sequence = open('CPLX2.txt', 'r')
CPLX2 = sequence.read()

count_A = 0
count_C = 0
count_T = 0
count_G = 0

for i in CPLX2:
    if CPLX2.startswith('>'):
        continue
    elif i == 'A':
        count_A = count_A + 1
    elif i == 'C':
        count_C = count_C + 1
    elif i == 'T':
        count_T = count_T + 1
    elif i == 'G':
        count_G = count_G +1

print('A:', count_A)
print('C:', count_C)
print('T:', count_T)
print('G:', count_G)