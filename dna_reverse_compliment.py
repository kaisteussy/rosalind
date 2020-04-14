
# In order to replace multiple characters simultaneously and to prevent the 're-conversion' of the newly translated
# characters, use the .translate() function!
with open('dna_reverse_compliment.txt') as f:
    reverse = f.read()
    reverse = reverse[len(reverse)::-1]
    reverse_compliment = reverse.translate(str.maketrans({'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}))
    print(reverse_compliment)
