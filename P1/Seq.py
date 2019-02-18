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
        return (result1)

    def reverse(self):
        return self.strbases[::-1]

    def count(self):
        bases = ['A', 'C', 'T', 'G']
        for i in bases:
            result2 = self.strbases.count(i)
            print(result2)

    def perc(self):
        cb = self.count(s)
        for i in self:
            result3 = (round(100.0 * cb[i] / len(self), 1))
            return (result3)