def reverse(sentence):
    words = sentence.split()
    revwords = reversed(words)
    resentence = ' '.join(revwords)
    return resentence

user = input()
sentence = reverse(user)
print(sentence)