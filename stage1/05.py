#Do the following conversions
#        •	(13)10 – (?)2, (?)8, (?)16
#        •  (0b10101001)2 – (?)10, (?)8, (?)16
#        •	(0o71)8 – (?)2, (?)10, (?)16
#        •	(0xE2F3)16 – (?)2, (?)8, (?)10

n = 13
print(bin(n))
print(oct(n))
print(hex(n))

print()

n='0b10101001'
n = int(n,2)
print(n)
print(oct(n))
print(hex(n))

print()

n='0o71'
n = int(n,8)
print(bin(n))
print(n)
print(hex(n))

print()

n='0xE2F3'
n = int(n,16)
print(bin(n))
print(oct(n))
print(n)