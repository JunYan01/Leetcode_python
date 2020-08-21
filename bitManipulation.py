
# print('A' | ' ' == 'a')
# print('b' & '_' == 'B')
# print('d' ^ ' ' == 'D')

# x = 'A' | ' '
# print(x)

x = -1
y = 2
f = ((x ^ y) < 0)
print(f)


x = 3
f = ((x ^ y) < 0)

print(f)

# print(-~x)

# print(~-x)

# x, y = 1, 2
# x ^= y
# y ^= x
# x ^= y
# print(x,y)

x = 2**12-1
res = 0
while x:
	x = x & (x-1)
	res += 1

print(res)

x = 2^12
# print(x&(x-1))

print((x&(x-1)) == 0)

