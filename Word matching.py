def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

    print("List of words with first and last letter the same are",lst)
    return ctr
count=match_words(['racecar','bob','twenty four','forty seven'])
print("Number of words having first and last letter the same",count)