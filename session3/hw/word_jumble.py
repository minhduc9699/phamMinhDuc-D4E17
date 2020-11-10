from random import shuffle
word = 'champion'
word = list(word)

print(word)
shuffle(word)
print(word)
quiz = ''
for w in word:
    quiz = quiz + w + ' '
print(quiz)
