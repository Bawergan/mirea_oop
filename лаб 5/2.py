import json
import matplotlib.pyplot as plt

with open('лаб 5/2.json', 'r', encoding="utf-8") as j: 
    json_data = json.load(j) 

name = "Иванов Иван Иванович 0"
year = 2010

x = []
y = []
for i in json_data["workers"]:
    if i["ФИО"] == name:
        for j in i["Выплаты"]:
            if int(j["Год"]) == year:
                x.append(j["Месяц"])
                y.append(int(j["Размер выплаты"]))

plt.bar(x, y, width=0.4, color = 'green')
plt.xlabel('месяц')
plt.ylabel('выплата')
plt.show()

year = 2011

x = []
y = []
payment_max = []
payment_min = []
for i in json_data["workers"]:
    payment = []
    for j in i["Выплаты"]:
        if int(j["Год"]) == year:
            payment.append(int(j["Размер выплаты"]))
    payment_max.append(max(payment))
    payment_min.append(min(payment))
    x.append(sum(payment)//len(payment))
    y.append(i["ФИО"])

plt.pie(x, labels= y)
plt.show()

width = 0.3
plt.bar([i - width for i in range(len(y))], payment_max, width, color = 'red')
#plt.bar([i for i in range(len(y))], x, width, color = 'green')
plt.bar([i + width for i in range(len(y))], payment_min, width, color = 'blue')
plt.xticks([i for i in range(len(y))], y)
plt.xlabel('workers')
plt.ylabel('payment')
plt.show()