# 6. Дано трехзначное число. 
# В нем зачеркнули первую слева цифру и приписали ее в конце. 
# Найти полученное число. 

a = 123

d1, d2, d3 = 0, 0, 0
d1 = a % 10
a //= 10
d2 = a % 10
a //= 10
d3 = a % 10
a = d2 * 100 + d1 * 10 + d3


print(a)