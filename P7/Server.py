import requests
import sys
from Seq_analyzer import Seq

server = "http://rest.ensembl.org"
ext = "/sequence/id/ENSG00000165879"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()

sequence = repr(decoded['seq'])
bases = ('A', 'C','T','G')
total = 0
maximum = ''

for i in bases:
   if Seq(sequence).count1(i) > total:
       total == Seq(sequence).count1(i)
       maximum = i


print('There are {} bases in FRAT1-gene.'.format(Seq(sequence).len()))
print('There are {} T bases in FRAT1-gene.'.format(Seq(sequence).count1('T')))
print('The most popular base in FRAT1-gene is {} and its percentage is {}.'.format(maximum,str(Seq(sequence).perc(maximum))+ '%'))
print('The percentage of T base is: {}.'.format(str(Seq(sequence).perc('T'))+ '%'))
print('The percentage of A base is: {}.'.format(str(Seq(sequence).perc('A'))+ '%'))
print('The percentage of G base is: {}.'.format(str(Seq(sequence).perc('G'))+'%'))
print('The percentage of C base is: {}.'.format(str(Seq(sequence).perc('C'))+'%'))
