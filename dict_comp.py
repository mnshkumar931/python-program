#sorting values using dic comprehension

dict={'a':1,'b':2,'c':1,'d':2,'e':3}

dict1={v:k for k,v in {v:k for k,v in dict.items()}.items()}
print(dict1)
# dict3={v:k for k,v in dict1.items()}
# print(dict3)