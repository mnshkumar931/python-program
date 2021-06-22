def list_primes(num):
    l=[2]
    for n in range(3,num,2):
        flag=0
        for i in range(2,n):
            if(n%i==0):
                flag=1
                break 
        else:
            if flag==0:
                l.append(n)
    
    return l




l1=list_primes(100)
print(len(l1))
print(l1)