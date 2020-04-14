def count_nucleotides(txt_file):
    molecule_count = ''
    with open(txt_file, 'r') as f:
        dna = f.read()
        molecule_count += str(dna.count('A')) + ' '
        molecule_count += str(dna.count('C')) + ' '
        molecule_count += str(dna.count('G')) + ' '
        molecule_count += str(dna.count('T')) + ' '
    return molecule_count


print(count_nucleotides('rosalind_ini7.txt'))



