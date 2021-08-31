class parent:
    def __init__(self,age1):
        self.age1=age1
    def show_age(self):
        return self.age1
b=parent(27)
print(b.show_age())
class child(parent):
    def name(self,name1):
        self.name1= name1
    def show_name(self):
        return self.name1
class child1(child):
    def gender(self,gender1):
        self.gender1=gender1
    def show_gender(self):
        return self.gender1

x=child1(27)

x.name('manish')
x.gender('male')
print(x.show_age())
print(x.show_name())
print(x.show_gender())