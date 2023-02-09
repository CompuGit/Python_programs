#WAP to find the rotated string
#Input : ABCD
#Ouput : ABCD BCDA CDAB DABC

text = 'ABCD'
broken = list(text)

for i in range(len(text)):
    print(''.join(broken), end=' ')
    x = broken.pop(0)
    broken.append(x)
