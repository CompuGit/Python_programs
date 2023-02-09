#WAP to Minimize the sum of an array where all its maximum numbers 
# will be reduced to half for the given k times.

k = int(input())
arr = input().split()

arr = [int(a) for a in arr]

for i in range(k):
	max_ = max(arr)
	arr[arr.index(max_)] = max_ // 2

total = sum(arr)
print(total)
