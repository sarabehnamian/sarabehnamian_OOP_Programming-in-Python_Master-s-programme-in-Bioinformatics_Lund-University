class SeqRecord(object):
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq
s = SeqRecord("MBG234Gag1", "AGCTGTCGGTAAGTCGAGT")     
print(s.name)   
print(s.seq)