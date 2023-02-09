#WAP to count characters and compress the given string.
#Input : aaaabbbccdaa
#Output: 4a3b2c1d2a

text = 'aaaabbbccdaa'
res = ''

#approach 1
first = text[0]
count=1
for i in range(1,len(text)):
    ele = text[i]
    if first!=ele:
            res = res + str(count)+first
            first = ele
            count = 1
    else:
            count+=1
else:
    res = res + str(count)+first

print(res)


#approach 2
'''i = iter(text)
first = next(i)

count = 1
while True:
    try:
        ele = next(i)
        if first!=ele:
            res = res + str(count)+first
            first = ele
            count = 1
        else:
            count+=1
        
    except StopIteration:
        res = res + str(count)+first
        break

print(res)'''