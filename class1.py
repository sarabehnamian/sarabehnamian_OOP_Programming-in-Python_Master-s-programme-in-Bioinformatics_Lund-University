 Exercise: Implement a Gene inheritance model
combining DNA
• A class representing a person. It has an attribute called “genes” which is string of letters. Each
character is a gene.
• Implement the + operator on genes that will create a new “Person” and for the gene will select
one randomly from each parent.
1 a = Person('ABC')
2 b = Person('DEF')
3 4
c = a + b
5 print(c.gene) # ABF
 
 
 Implement a Gene inheritance model
combining DNA
1 import random
2 3
class Person(object):
4 def __init__(self, DNA):
5 self.DNA = DNA
6 7
def gene(self):
8 return list(self.DNA)
9
10 def print_genes(self):
11 print(list(self.DNA))
12
13 def __add__(self, other):
14 DNA_father = self.gene()
15 DNA_mother = other.gene()
16 if len(DNA_father) != len(DNA_mother):
17 raise Exception("Incompatible couple")
18
19 DNA_childPosible_sequence = DNA_father + DNA_mother
20 DNA_child = ""
21 for i in range(len(self.gene())):
22 DNA_child += random.choice([DNA_father[i], DNA_mother[i]])
23
24 return Person(DNA_child)
25
26
27 a = Person("ABCD")
28 b = Person("1234")
29 c = a + b
30 print(c.DNA)