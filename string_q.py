class string():
    def __init__(self,str,k):
        self.str=str
        self.k=k
    def something(self):

        d=[n for n in self.str]
        print(d)
        x=''
        if len(self.str)%2==0:
              for i in range(0,len(self.str),self.k):
                  x=x+self.str[i+1]+self.str[i]
              return x
        else:
             for i in range(0,len(self.str)-self.k-1,self.k):
                x=x+self.str[i+1]+self.str[i]
             return x+self.str[-1]

            
a=input('enter a first string')
b=int(input('enter the value of k'))
x=string(a,b)
print(x.something())