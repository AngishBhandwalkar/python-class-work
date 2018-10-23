import random
from random import randint as rt
def game(dice,faces):
    result=0
    for roll in range(0,dice):
        result+=rt(1,faces)
        return result
result=game(1,6)
print(result)
