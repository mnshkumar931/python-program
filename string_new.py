
def pattern(seq):
    x=''
    if len(seq)%2==0:
        for i in range(0,len(seq),2):
            x=x+seq[i+1]+seq[i]
        return x
    else:
        for i in range(0,len(seq)-1,2):
            x=x+seq[i+1]+seq[i]
        return x+seq[-1]

print(pattern('manisha'))
