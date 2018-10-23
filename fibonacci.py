#Angish bhandwalkar 11810766 M03
n=int(input())
l=[]
a=0
b=1
count=1
if n==0:
    print("s1")
elif n==1:
    print('0','1')
else :
    l.append(0)
    l.append(1)
    while count<=n-2:
       l.append(a+b)
       c=a+b
       a=b
       b=c
       count+=1
print(l)       
    
