#Find the length of bits occupied, number of 1’s and 0’s in a given integer n = 158 

n = 158

print( n.bit_length() ) #max bits used
print( n.bit_count() ) #1 bits in n
print( n.bit_length() - n.bit_count() ) #0 bits in n