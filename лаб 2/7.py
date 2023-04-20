# 7. Дано трехзначное число, в котором все цифры различны. 
# Получить шесть чисел, образованных при перестановке цифр заданного числа.

a = 123

d1, d2, d3 = 0, 0, 0
d1 = a % 10
a //= 10
d2 = a % 10
a //= 10
d3 = a % 10

a = [d3, d2, d1]

b = []
for i in range (3):
    for j in range(3):
        for k in range(3):
            if j == i or k == i or k == j: continue
            b.append(a[i] * 100 + a[j] * 10 + a[k])

print(b)