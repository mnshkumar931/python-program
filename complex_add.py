class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def add(self):
        x1,x2 = self.real
        y1,y2 = self.img
        r = x1+x2
        i = y1+y2
        print(f'{r} + {i}i')
r1 = (4,5)
i1 = (2,4)
d = Complex(r1, i1)
d.add()
