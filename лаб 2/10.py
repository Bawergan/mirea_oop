# 10. В трехзначном числе x зачеркнули его вторую цифру. 
# Когда к образованному при этом двузначному числу справа 
# приписали вторую цифру числа x, то получилось число 456. 
# Найти число x.

n = 456
print(n // 100 * 100 + n % 10 * 10 + n // 10 % 10)