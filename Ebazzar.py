

from easygui import*
import sys
while 1:
  msgbox("welcome to e-bazar")
  i=buttonbox("which product do you want?","available products",choices=("chocolate","biscuit","soap"))
  if i=="chocolate":
      j=buttonbox("which chocolate do you want?","available chocolates",choices=("kitkat","munch","perk"))
      if j=="kitkat":
       k=buttonbox("from where to buy?","available vendors",choices=("bigbazar=Rs 10","d mart=Rs 9.5"))
      elif j=="munch":
       k=buttonbox("from where to buy?","available veendors",choices=("bigbazar=Rs 4.5","d mart=Rs 5"))
      elif j=="perk":
       k=buttonbox("from where to buy?","available vendors",choices=("bigbazar=","d mart=")) 
  elif i=="biscuit": 
      j=buttonbox("which biscuit do you want?","available biscuits",choices=("oreo","marie","bourbon")) 
      if j=="oreo":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=","d mart="))
      elif j=="marie":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=","d mart="))
      elif j=="bourbon":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=","d mart="))
  elif i=="soap":
      j=buttonbox("which soap do you want?","available soaps",choices=("fiama","medimix","pears"))
      if j=="fiama":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=","d mart="))
      elif j=="medimix":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=","d mart="))
      elif j=="pears":
       k=buttonbox("from where to buy","available vendors",choices=("bigbazar=","d mart="))
  msgbox("You chose: " + str(choice), "Survey Result")

  msg = "Do you want to continue?"
  title = "Please Confirm"
  if ccbox(msg, title):     # show a Continue/Cancel dialog
      pass  # user chose Continue
  else:
      sys.exit(0)
