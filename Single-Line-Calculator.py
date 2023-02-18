# Simple Calculator. 
# Program Structure: supporting functions and a main function
# Modules: Used.

import string
from math import factorial

all_inputs = []

def clear():
    global all_inputs 
    all_inputs = []
    print("Previous calculated output/inputs entered cleared.")
    
         
def add(*args):
    return sum(*args)

def sub(args):
    out = args[0]
    for x in args[1:]:
        out -= x
    return out 

def mul(args):
    out = 1
    for x in args:
        out *= x
    return out 


def div(args):
    out = args[0] 
    for num in args[1:]:
        out /= num
    return out 

def display(num):
         print("Display: " + str(num))

def intermediate(num):
     if type(num) is float or type(num) is int:
         all_inputs.append(num)
     display(num)

def operand(symbol):
    global all_inputs
    out = {'+':add,'-':sub,'*':mul,'/':div,'!':factorial}
    all_inputs = [out[symbol](all_inputs[:len(all_inputs)])]
    display(all_inputs[0])

def simple_calculator():
    global all_inputs
    while True:

       curr_input = input("Simple Calculator: ")
       for letter in curr_input: 
           if letter in string.ascii_lowercase + string.ascii_uppercase + "#$%&'(),:;<>@[\]^_`{|}~" + '"':
               print('Ensure only float/integer is allowed')
               continue
       
       if curr_input == '?':
           instructions()
           continue
      
       if curr_input == 'clear' or curr_input == 'clr':
           clear()
           continue

       if len(all_inputs) >= 1:
           if curr_input == '+': 
               operand('+')
               continue
           elif curr_input == '-':
               operand('-')
               continue
           elif curr_input == '*':
               operand('*')
               continue
           elif curr_input == '/':
               operand('/')
               continue
           elif curr_input == "!":
               print("Last input counts only, converted to integer")
               # del all_inputs[:len(all_inputs) - 1]      
               all_inputs = [factorial(int(all_inputs[-1]))]
               intermediate(all_inputs[0])           
               continue

           if curr_input == '=':
               print('Ans: ', all_inputs[0])
               exit()

       curr_input = float(curr_input)
       intermediate(curr_input)
        

def instructions():
    print('++ These are instructons for usage: ++')
    print('Input values on a single line.')
    print('Operators Available: + - / * ! ')
    print("For Evaluation use: = , answer will be given with 'ans' ") 
    print('A list of numbers can be given separated on a new line and than an operator at the end.') 
    print('Numbers and operators can be given as well and will be evaluated as requied.')
    print('Exceptions, can occur. If a nonsensical value is given/not feasible.')
    print("Type: 'clear' or 'clr' to clear the last calculated output remembered for the next calculation.") 
    print("Type: '?' to see this message again.") 
    print()

if __name__ == '__main__':
    print('---- Simple Calculator ----')
    instructions()
    simple_calculator()

