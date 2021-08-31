def deco():
    print('my name is manish')
def other_deco():
    print('it is second deco')
    print(deco())
m=other_deco()
print(m)
