#WAP to find all the trailing numbers from the given list whose sum exactly equals k
#Input : arr = [5,3,8,2,1,10,1]; k = 11
#output : [3, 8] [8, 2, 1] [1, 10] [10, 1]


arr = [5,3,8,2,1,10,1]

n = len(arr)
k=11

results = []

for i in range(n):
    lst = []         
    for j in range(i, n):
        lst.append(arr[j])

        if sum(lst) == k:
            results.append(lst)
            break

for lst in results:
	print(lst)
