def fibbonacci(num):
    n1,n2=0,1
    count=0
   
    if num<=0 :
        print('enter a postive number' )
    # elif num==1:
        # print(n1)
    else: 
        while count<num:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
            
        
            
a=int(input('enter the value of n\n'))
fibbonacci(a)



           

        