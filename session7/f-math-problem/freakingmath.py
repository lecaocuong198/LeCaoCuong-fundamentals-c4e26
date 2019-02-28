# from random import *

# def generate_quiz():
#     # Hint: Return [x, y, op, result]
#     return [0, 0, '@@', 12]

# def check_answer(x, y, op, result, user_choice):
#     pass
from random import *
import calc

def generate_quiz():
    # Hint: Return [x, y, op, result]

    x = randint(0,9)
    y = randint(1,9)
    op = choice(['+','-','*','/'])
    result = calc.evaluate(x,y,op) + randint(-1,1)
    return [x,y, op, result]

def check_answer(x, y, op, result,user_choice):
    if calc.evaluate(x,y,op) == result:
        if user_choice == True:
            return True
        else:
            return False
    else:
        if user_choice == False:
            return True
        else:
            return False