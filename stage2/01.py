#WAP to reverse the words in a string and capitalize the first letter
#Input : 'I am a boy'
#Output : 'Boy a am i'

text = 'I am a boy'
words = text.split()
words = words[::-1]
text = ' '.join(words)
text = text.capitalize()

print(text)