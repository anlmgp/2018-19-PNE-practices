from Seq import Seq

Sequence1 = Seq( "AGTACACTGGT")
Sequence2 = Seq ("CGTAAC")
Sequence3 = Sequence1.complement()
Sequence4 = Sequence3.reverse()

Sequences = [Sequence1, Sequence2, Sequence3, Sequence4]
Bases = ['A','T','G','C']
number = 0
for i in Sequences:
    number = number + 1
    print('Sequence {}:'.format(number),i.strbases)
    print('  Length: {}'.format(i.len()))
    for s in Bases:
        print('  Bases count: {}'.format(i.count(s)))
        print('  Bases percentage: {}'.format())