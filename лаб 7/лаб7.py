class client:
    __balance = 0
    sername, name, = '', '' 
    age = 0

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
    
    def Validator(self, sum):
        return (self.__balance + sum) >= 0        
    
    def OperationManager(self, sum):
        if self.Validator(sum): self.__EditBalance(sum)
        else: print('Operation invalid')
    

class transaction:
    transactionSum = 0

    def __init__(self, transactionSum):
        self.transactionSum = transactionSum
    
    def Commision(self, comisionPersent):
        return self.transactionSum * (1 - comisionPersent/100) 


sergey = client(sername='Gavrilushkin', name='Sergey', age=10, balance=100)
print(sergey.Info())

sergey.OperationManager(transaction(-200).Commision(10))
print(sergey.Info())

sergey.OperationManager(100)
sergey.OperationManager(transaction(-200).Commision(10))
print(sergey.Info())