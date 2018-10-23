#Angish bhandwalkar 11810766 M03
x=int(input())
a=x
sum=0
while a>0:
    n=a%10
    sum=sum+n**3
    a=a//10
print(sum)
if sum==x:
       print("it is a arm")
else :
    print("it is not a arm")
