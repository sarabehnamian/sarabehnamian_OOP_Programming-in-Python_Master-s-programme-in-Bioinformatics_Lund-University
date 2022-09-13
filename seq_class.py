import re

class NuclSequence :
    def __init__ (self , sequence ):
        self .seq = sequence

    def getRevComp ( self ):
  # Retrieve the reverse complement for the sequence
  # The -1 tells Python to begin from the end of the string :
        rev_low_seq = self .seq [:: -1]. lower ()
        return rev_low_seq . translate ( str . maketrans ('atgc ','tgca '))

    def getOligoCount (self , oligo ):

    # Counts the number of oligo occurrences in the sequence . Counts both for forward and reverse strands
        fw_count = len(re. findall (oligo , self .seq , re.I))
        rv_seq = self . getRevComp ()
        rv_count = len(re. findall (oligo , rv_seq , re.I))
        return fw_count + rv_count

    def __str__ ( self ):
        return self . seq