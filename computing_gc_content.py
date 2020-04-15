# modified read_fasta() function from BioPython
# First application of yield to get multiple value pairs out of a function!


def calculate_gc_percentage(dna_string):
    gc_count = 0
    for letter in dna_string:
        if letter == 'C' or letter == 'G':
            gc_count += 1
    gc_percentage = (gc_count / (len(dna_string))) * 100
    return gc_percentage


def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                yield name, calculate_gc_percentage(''.join(seq))
            name, seq = line.lstrip('>'), []
        else:
            seq.append(line)
    if name:
        yield name, calculate_gc_percentage(''.join(seq))


with open('computing_gc_content.txt') as fp:
    highest_gc, highest_name = float('-inf'), ''
    for name, gc in read_fasta(fp):
        if gc > highest_gc:
            highest_gc, highest_name = gc, name
    print(highest_name + '\n' + str(highest_gc))
