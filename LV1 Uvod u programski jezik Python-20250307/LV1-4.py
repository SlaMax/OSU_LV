rijeci ={}

fsong= open('song.txt')

for line in fsong:
    line = line . rstrip ()
    words = line . split ()
    for word in words:
        if word in rijeci:
            rijeci[word]+=1
        else:
            rijeci[word]=1    

for word in words:
    if rijeci[word] == 1 :
        print(word)