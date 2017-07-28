print
word = raw_input("Enter a word you would like reversed")
num = len(word)-1
newWord = ""
for x in range(len(word)):
    stri = word[x+num]
    num = num-2
    newWord = newWord + stri

print newWord