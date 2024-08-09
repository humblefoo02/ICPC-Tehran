a = int(input())
b = int(input())
c = int(input())
d = int(input())

rec_a = a-b
rec_b = c-d

if rec_a < rec_b:
    print('Namakestan')
elif rec_a == rec_b:
    print('Equal')
else:
    print('Shekarestan')