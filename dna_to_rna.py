import regex as re

with open('dna_to_rna.txt', 'r') as f:
    rna = f.read().replace('T', 'U')
    print(rna)


# With regex!
# with open('dna_to_rna.txt', 'r') as f:
#     rna = re.sub('T', 'U', f.read())
#     print(rna)
