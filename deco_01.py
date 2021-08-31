def fuc(name='manish'):
    print("i m inside the hello function")
    def greet():
        return "/t i m inside greet function"

    def welcome():
        return "/t i m inside welcome function"

    print('i m going to return a function' )

    if name=='manish':
        return greet
    else:
        return welcome
my_func=fuc('manish')
print(my_func)
print(my_func())



