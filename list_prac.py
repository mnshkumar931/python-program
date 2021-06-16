l = [1,3,5,9,2,3,4,9]
count=0
for i in range(0,len(l)-3):
    if(l[i]+l[i+1]+l[i+2]==l[i+3]):
        count+=1 
print(count)    