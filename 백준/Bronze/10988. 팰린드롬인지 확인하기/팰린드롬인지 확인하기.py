word=input()
word=list(word)
reverse_word=list(reversed(word))
if(word==reverse_word):
    print(1)
else:
    print(0)