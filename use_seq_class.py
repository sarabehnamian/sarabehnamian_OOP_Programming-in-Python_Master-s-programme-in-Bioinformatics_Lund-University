import sys
import seq_class

target_oligo = sys.argv[1]
in_fh = open(sys.argv[2] , 'r')

count = 0
for line in in_fh:
    line = line.rstrip()
    if not line: continue

    if not line[0] == '>':
     # Create sequence object
       seq_obj = seq_class.NuclSequence( line )

    # Retrieve oligo count for + and - strands
       count += seq_obj.getOligoCount( target_oligo )
print ('Oligo occurrences : {} '.format( count ))