words = "olly olly in come free"


wordlist = words.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))


print( str(zip(wordlist, wordfreq)))

