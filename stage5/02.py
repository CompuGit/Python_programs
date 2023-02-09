#WAP to print the following pattern
#*******
# *****
#  ***
#   *

#approach 1
n = 4
for i in range(n):
    print(' '*i, end='')

    for j in range(2*n-1):
        print('*',end='')
    
    print()
    n-=1

#approach 2
n = 4
k = 2*n-1
for i in range(k,0,-2):
    print(format('*'*i,f'^{k}'))