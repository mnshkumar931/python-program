import random 
a = random.randint(100,999)
print(a)

while True:
    x=int(input('enter a three digit number\n'))
    if  x > a:
        print('you guessed higher number')
    elif x < a:
        print('you guessed lower number')
    elif x==a: 
        print('you crack the code')
        break
        