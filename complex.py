class complex:
    def __init__(self,real1,real2,img1,img2):
        self.real1=real1
        self.real2=real2
        self.img1=img1
        self.img2=img2
    def add(self):
        return (f'{self.real1 + self.real2} + {self.img1+self.img2}i')
a=int(input('enter first real number\n'))
b=int(input('enter first imag number\n'))
c=int(input('enter second real number\n'))
d=int(input('enter second imag number\n'))
x=complex(a,b,c,d)
print(x.add())