class Seq:

    def __init__(self, strbases):
        self.strbases = strbases

    def len (self):
        return len(self.strbases)

    def complement(self):
        bases = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        result1 = []
        for i in self.strbases:
            if i in bases:
                result1.append(bases[i])
        result1 = "".join(result1)
        return Seq(result1)

    def reverse(self):
        return Seq(self.strbases[::-1])

    def count(self, base):
        counter = []
        result2 = []
        for i in base:
            r = self.count(i)
            counter.append(r)
        result = dict(zip(base, counter))
        for key, value in result.items():
            s = key + ':' + str(value)
            result2.append(s)
        result2 = ", ".join(result2)
        return (result2)

    def perc(self, base ):
        cb = self.count(base)
        for i in self:
            result3 = (round(100.0 * cb[i] / len(self), 1))
            return (result3)