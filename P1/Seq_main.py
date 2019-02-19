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
    counter = []
    m = []
    counter2 = []
    h = []
    for s in Bases:
        r = i.count1(s)
        counter.append(r)
        result = dict(zip(Bases, counter))
        for key, value in result.items():
            s = str(key + ':' + str(value))
        m.append(s)
        result2 = ", ".join(m)
    print('  Bases count: {}'.format(result2))
    for s in Bases:
        t = i.perc(s)
        counter2.append(t)
        resultt = dict(zip(Bases, counter2))
        for key, value in resultt.items():
            s = str(key + ':' + str(value))
        h.append(s)
        result4 = " %, ".join(h)

    print('  Bases percentage: {}%'.format(result4))


