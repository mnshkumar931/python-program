import random
a = random.randint(1,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = str(a) + str(b) + str(c)
l=[n for n in d]
print(l)

flag=True
while flag:
     my_number = input('enter a three digit number\n')
     l1=[n for n in my_number ]
     print(l1)
     if l[::] == l1[::]:
        print('you crack the code')
        flag=False
     elif l[0]==l1[0] and l[1] != l1[1] and l[2] != l1[2] :
         print('your 100th digit is only correct')
        
     elif l[0]!=l1[0] and l[1] == l1[1] and l[2] != l1[2] :
         print('your 10th digit is  only correct')
       
     elif l[0]!=l1[0] and l[1] != l1[1] and l[2] == l1[2] :
         print('your unit digit is only correct')
        
     elif l[0]==l1[0] and l[1] == l1[1] and l[2]!=l1[2]:
         print('your unit digit is incorrect')
        
     elif l[0]==l1[0] and l[1] != l1[1] and l[2]==l1[2]:
          print('your 10th digit is incorrect')
        
     elif l[0]!=l1[0] and l[1] == l1[1] and l[2]==l1[2]:
          print('your 100th digit is incorrect')
          
     else:
         print("none of the digits match")


