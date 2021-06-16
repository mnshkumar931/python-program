class Animal():
    type='pet'

    def __init__(self,dog,cat):
        print('parent cons called')
        self.dog=dog
        self.cat=cat
    def speak(self):
        print(self.dog +" dog bark")
        print(self.cat +" cat meow")
    def info(self,name,age):
        print(f'{name}  {age}')
    
# x=Animal("felix","pussy")
# y=Animal("mike","pont")

# print(x.type)
# print(y.type)
# print(Animal.type)

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__('dog','cat')
        print('child cons called')
        self.name=name
        self.breed=breed
    
    def info(self,name,age):
        print(f'{name}  {age}')

d=Dog('monty','huskie')
# a=An imal('dog','cat')
# d.info('dog1',2)
# d.info('dog2',4,'M')
# d.info('gog3',5,'F','black')
