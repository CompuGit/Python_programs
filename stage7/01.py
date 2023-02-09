#WAP to count the repeated words in a string
#Input : 'abc bca cba cab abc acb bca acb'
#Output : abc=2 bca=2 cba=1 cab=1 acb=2

text = 'abc bca cba cab abc acb bca acb'
words = text.split()
unique_words = set(words)

res = {}

for word in unique_words:
    res[word] = words.count(word)


for k,v in res.items():
    print(f'{k}={v}',end=' ')