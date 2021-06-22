my_array=[5,2,6,7,8]#by simple method
sum=0
for item in my_array:
    sum=sum+item
print(sum)
# by using function 
def sum_of_array(*argv):
    sum=0
    for item in argv:
        sum=sum+item
    return sum
a=sum_of_array(3,4,5,3,8,6,9,2,45,76,45,98)
print(a)
