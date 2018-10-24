#angish bhandwalkar 11810766 M03

from easygui import*
import sys
sum=0
list=[]
while 1:
  msgbox("welcome to e-bazar")
  i=buttonbox("which product do you want?","available products",choices=("chocolate","biscuit","soap"))
  if i=="chocolate":
      j=buttonbox("which chocolate do you want?","available chocolates",choices=("kitkat","munch","perk"))
      if j=="kitkat":
       k=buttonbox("from where to buy?","available vendors",choices=("bigbazar=Rs 10","d mart=Rs 9.5"))
       if k=="bigbazar=Rs 10":
            sum+=10
            list.append(k)
       elif k=="d mart=Rs 9.5":
            sum+=9.5
            list.append(k)
      elif j=="munch":
       k=buttonbox("from where to buy?","available veendors",choices=("bigbazar=Rs 4.5","d mart=Rs 5"))
       if k=="bigbazar=Rs 4.5":
            sum+=4.5
            list.append(k)
      elif j=="perk":
       k=buttonbox("from where to buy?","available vendors",choices=("bigbazar=5","d mart=7"))
       if k=="bigbaar=Rs5":
            sum+=5
            list.append(k)
       elif k=="d-mart=7":
            sum+=7
            list.append(k)
  elif i=="biscuit": 
      j=buttonbox("which biscuit do you want?","available biscuits",choices=("oreo","marie","bourbon")) 
      if j=="oreo":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=12","d mart=10"))
       if k=="bigbazar=12":
            sum+=12
            list.append(k)
       elif k=="d mart=10":
            sum+=10
            list.append(k)
      elif j=="marie":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=6","d mart=8"))
       if k=="bigbazar=6":
            sum+=6
            list.append(k)
       elif k=="d mart=8":
            sum+=8
            list.append(k)
      elif j=="bourbon":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=10","d mart=15"))
       if k=="bigbazar=10":
            sum+=10
            list.append(k)
       elif k=="d mart=15":
            sum+=15
            list.append(k)
  elif i=="soap":
      j=buttonbox("which soap do you want?","available soaps",choices=("fiama","medimix"))
      if j=="fiama":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=50","d mart=60"))
       if k=="bigbazar=50":
            sum+=50
            list.append(k)
       elif k=="d mart=60":
            sum+=60
            list.append(k)
      elif j=="medimix":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=30","d mart=20"))
       if k=="bigbazar=30":
            sum+=30
            list.append(k)
       elif k=="d mart=20":
            sum+=20
            list.append(k)
     
  msgbox("You chose: " + str(j) + str(k), "customer cart")

  msg = "Do you want to continue?"
  title = "Please Confirm"
  if ccbox(msg, title):     # show a Continue/Cancel dialog
      pass  # user chose Continue
  else:
      print(sum,list)

