from pathlib import Path

# Not entirely necessary to import Path, as opposed to using the text file's name directly since they are in the same
# directory
data_folder = Path('C:/Users/Bamboozle/PycharmProjects/rosalind')
file_to_open = data_folder / "rosalind_ini5.txt"
count = 0

with open(file_to_open, 'r') as f:
    for line in f:
        count += 1
        if count % 2 == 0:
            print(line)

# readline() skips to the next line, which results in every other line as well!
# with open('rosalind_dna.txt', 'r') as f:
#     for line in f:
#         print(f.readline())
