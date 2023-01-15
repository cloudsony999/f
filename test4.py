def add(a,b):
    return a+b

def sub(a,b):
    return a-b



print('sum is ',add(12,34))

print('sub is ',sub(356,34))

def calc(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e

z=calc(22,10)
print(type(z))

print(z)
print(z[0],z[1],z[2])

for i in z:
    print(i)


