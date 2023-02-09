#3.	Find number of sentences, words, letters, spaces in the given statement.
#'The quick brown fox jumps over a lazy dog. 1234567890.'

statement = 'The quick brown fox jumps over a lazy dog. 1234567890.'

sentences = statement.count('.')
words = len(statement.split(' '))
spaces = words-1
letters = len(statement) - spaces

print('sentences =',sentences)
print('words =',words)
print('letters =',letters)
print('spaces =',spaces)