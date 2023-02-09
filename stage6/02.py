#WAP to find given anagram available in the other string, if yes print their indices.
#Input : 'baccbbbdabcdbca' 'abc'
#Output : [0,8,12]

m = 'baccbbbdabcdbca'
n = 'abc'

every_n = []
for i in range(len(m)):
    every_n.append(m[i:i+len(n)])

indices = []
for ele in every_n:
    if sorted(ele)==sorted(n):
        indices.append(every_n.index(ele))

print(indices)

'''everyn = [ m[i:i+len(n)] for i in range(len(m))]

res = [ everyn.index(ele) for ele in everyn if sorted(ele)==sorted(n)]

print(res)'''