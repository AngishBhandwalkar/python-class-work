#Angish Bhandwalkar M03 11810766
y=int(input("enter the year"))  
if y%4==0:
 if y%100==0:
  if y%400==0:
   print(" leap year")
  else :
    print("not a leap year")
 else : 
  print(" a leap year")
else:
 print("not a leap year")
