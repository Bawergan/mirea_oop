# 9. Работа светофора для пешеходов запрограммирована следующим образом: в начале 
# каждого часа в течение трех минут горит зеленый сигнал, затем в течение двух минут—
# красный,  в  течение  трех  минут  —опять  зеленый  и  т.д.  Дано  вещественное  число  t, 
# означающее время в минутах, прошедшее с начала очередного часа. Определить, сигнал 
# какого цвета горит для пешеходов в этот момент.  

t = 39
t %= 5

print('горит {} цвет'.format(('красный', 'зеленый')[t<4]))