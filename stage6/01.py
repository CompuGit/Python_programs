#WAP to find min and max number in an array and print in (min,max) tuple format.
#Input : [2,4,5,1,3]
#ouput : (1,5)

arr = [2,4,5,1,3]

min_e = max_e = arr[0]

for i in range(1,len(arr)):
    ele = arr[i]
    if ele<min_e:
        min_e = ele
    if ele>=max_e:
        max_e = ele

res = (min_e,max_e)

print(res)