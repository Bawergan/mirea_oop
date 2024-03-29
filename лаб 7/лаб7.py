class client:
    def __init__(self, sername, name, age, balance):
        self.sername = sername
        self.name = name
        self.age = age
        self.__balance = balance

    def Info(self):
        return {'sername' : self.sername, 
                'name' : self.name, 
                'age' : self.age,
                'balance' : self.__balance}
    
    def __EditBalance(self, sum):
        self.__balance += sum
        print(f'{self.name} edited: {sum}')
    
    def Validator(self, sum):
        return (self.__balance + sum) >= 0        
    
    def OperationManager(self, sum):
        print(f'from {self.name} asked operation {sum}')
        if self.Validator(sum): self.__EditBalance(sum)
        else: print(f'Operation {sum} invalid')
    
    def Transaction(self, clientToTransaction, sum, commisionPersent = 10):
        print (f'from {self.name} to {clientToTransaction.name} asked transaction {sum}, {commisionPersent}%')
        if self.Validator(-sum):
            self.OperationManager(-sum)
            clientToTransaction.OperationManager(transaction(sum).Commision(commisionPersent))
        else: print(f'Transaction {sum} invalid')

class transaction:
    def __init__(self, transactionSum):
        self.transactionSum = transactionSum
    
    def Commision(self, comisionPersent):
        print(f'commision: {self.transactionSum * comisionPersent/100}')
        return self.transactionSum * (1 - comisionPersent/100) 



#создаем пользователя 1
sergey = client(sername='Gavrilushkin', name='Sergey', age=10, balance=100)
print(sergey.Info())
print('-'*100)

#изменяем баланс
sergey.OperationManager(50)
print('balance:', sergey.Info()['balance'])

sergey.OperationManager(-25)
print('balance:', sergey.Info()['balance'])

print('-'*100)

#создаем пользователя 2
andrey = client(sername='', name='andrey', age=18, balance=100)

print(sergey.Info())
print(andrey.Info())

print('-'*100)

#делаем невалидный перевод (недостаточно средств)
andrey.Transaction(clientToTransaction=sergey, sum=1000)

print('-'*100)

andrey.OperationManager(1000)

#делаем валидный перевод
andrey.Transaction(clientToTransaction=sergey, sum=1000)

print('-'*100)

print(sergey.Info())
print(andrey.Info())
