class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
        num1=num2=0
    def add(self):
        
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1 / self.num2
    def mod(self):
        return self.num1 % self.num2


a=int(input('enter a value of first number \n'))
b=int(input('enter the value of second number\n'))
x=calculator(a,b)
print(x.add())
print(x.sub())
print(x.mul())
print(x.div())
print(x.mod())
