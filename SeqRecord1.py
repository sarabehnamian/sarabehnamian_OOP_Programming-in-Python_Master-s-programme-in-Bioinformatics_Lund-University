class SeqRecord(object):
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq
    def fasta_string(self):
        string_rep = ">" + self.name + "\n"
        string_rep += self.seq + "\n"
        return string_rep

s = SeqRecord("MBG234Gag1", "AGCTGTCGGTAAGTCGAGT")     
print(s.fasta_string())
