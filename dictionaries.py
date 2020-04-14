unique_wl = []

# Opens a txt file with a single line and counts the number of occurrences of each unique word
with open('rosalind_ini6.txt', 'r') as f:
    wordstring = f.read()
    wordlist = wordstring.split()
    for word in wordlist:
        if word not in unique_wl:
            print(word + ' ' + str(wordlist.count(word)))
        unique_wl.append(word)





# Manually, without opening a .txt file.
#
# wordstring = 'We tried list and we tried dicts also we tried Zen'
#
# wordlist = wordstring.split()
# unique_wl = []
#
# for word in wordlist:
#     if word not in unique_wl:
#         print(word + ' ' + str(wordlist.count(word)))
#     unique_wl.append(word)
