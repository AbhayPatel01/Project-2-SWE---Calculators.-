# Simple Handheld Calculator. 

# Modules: Used, GUI Programming. 
# Program Structure: Simple, Support and main function.
# Style: OOP; string lists and callbacks. 

# Idea 1.
  # Learn tikinter/tck/tcl module [just enough to make the program work] learn the module, more indepth.
  # Step 1: Create the UI.
  # Step 2: Create the Logic that fits the UI.  

# TO DO: 
    # Add appropriate font symbols.
    # Make a efficient parser, symbolic (Make it dual) e.g. google product. 
    # Make a history, tracker/interactive (Develop A system, appropriate DB, etc..);
    # Make themes, colors, to chose from. 
    # Graphical Feature, Conversion Features,maximises to more buttons; e.g. Mac calculator.
    # Design the Software Program differently, more efficient: Incorporate Algorithms and datastructures, sys design,modules,architecture, etc..
    # Make UX/UI easy to use, intuitive, consistent. UI/UX principles; add more buttons. 
    # Good Coding Practices: Workflow for development, Comments, Refactor Code, More Tests, Efficient/Effective Calculations.
    # Have 3 Error Handling mechanisms: e.g. Error, Infinity, Undefined
    # Use Differeht Technologies, Language, libraries. 
    # Intuitive arithmetic, e.g. algebraic expressions usally multiplied for paranthesis.     


# Cross Platform 
# Symbolic, without parser.

from tkinter import *
from tkinter import ttk
import re
import random
import webbrowser

class Calculator():
    ''' A Simple Handheld Calculator''' 
    operators = ['+', '-','×','÷'] 

    def __init__(self, root):

        root.title("Calculator")
        mainframe = ttk.Frame(root, padding="4 5 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.resizable(0,0)        

        self.display = StringVar()
        calculator_display = ttk.Entry(mainframe, width=40, textvariable = self.display)
        calculator_display.configure(state='disabled', justify='right')
        calculator_display.configure(foreground="black", background="white")
        calculator_display.grid(column=0,row=1,columnspan=5,rowspan=1,sticky=E)

        
        # Basic buttons.
        ttk.Button(mainframe,text='AC', command=lambda: self.clear(calculator_display)).grid(column=0,row=11,sticky=N)
        ttk.Button(mainframe,text='CE', command=lambda: self.backspace('')).grid(column=0,row=12,sticky=N)

        ttk.Button(mainframe,text='+/-', command=lambda: self.sign('')).grid(column=1,row=12,sticky=N)
        ttk.Button(mainframe,text='%', command=lambda : self.percent('')).grid(column=2,row=12,sticky=N)

        ttk.Button(mainframe,text='×', command=lambda : self.calculate('×')).grid(column=3,row=12,sticky=N)
        ttk.Button(mainframe,text='-', command=lambda : self.calculate('-')).grid(column=3,row=13,sticky=N)
        ttk.Button(mainframe,text='+', command=lambda : self.calculate('+')).grid(column=3,row=14,sticky=N)
        ttk.Button(mainframe,text='÷', command=lambda : self.calculate('÷')).grid(column=3,row=15,sticky=N)
        ttk.Button(mainframe,text='=', command=lambda : self.calculate('=')).grid(column=3,row=16,sticky=N)
       
         
        ttk.Button(mainframe,text='(', command=lambda : self.put('(')).grid(column=1,row=11,sticky=N)
        ttk.Button(mainframe,text=')', command=lambda : self.put(')')).grid(column=2,row=11,sticky=N)

         
        random_button =[
        ttk.Button(mainframe,text='Wiki', command=lambda: webbrowser.open_new('https://en.wikipedia.org/wiki/Calculator')), 
        ttk.Button(mainframe,text='HPC', command=lambda : webbrowser.open_new('https://keisan.casio.com/calculator')),
        ttk.Button(mainframe,text='Walph', command=lambda : webbrowser.open_new('https://www.wolframalpha.com')),
        ttk.Button(mainframe,text='Vint', command=lambda : webbrowser.open_new('http://www.vintagecalculators.com/html/mechanical_calculators.html')),
        ttk.Button(mainframe,text='Super', command=lambda : webbrowser.open_new('https://en.wikipedia.org/wiki/Supercomputer')),
        ttk.Button(mainframe,text='Comic', command=lambda : webbrowser.open_new('https://xkcd.com'))]
        random_button[random.randrange(0,len(random_button) - 1)].grid(column=3,row=11,sticky=N)

        # TO DO. (Add More Buttons/Features To The Calculator.)
        # ttk.Button(mainframe,text='', command=lambda : self.).grid(column=3,row=16,sticky=N)
        # ttk.Button(mainframe,text='', command=lambda : self.).grid(column=3,row=16,sticky=N)
        # ttk.Button(mainframe,text='', command=lambda : self.).grid(column=3,row=16,sticky=N)
        
        # ttk.Button(mainframe,text=')', command=lambda : self.put(')')).grid(column=3,row=16,sticky=N)
        #Dual Symbolic and without symbols, button. 
        # ttk.Button(mainframe,text='-', command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        
        # ttk.Button(mainframe,text='x', command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text='x', command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)

        # ttk.Button(mainframe,text='=', command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text='=', command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text='=', command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text='=', command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)

        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        # ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
       
        ttk.Button(mainframe,text=7, command=lambda : self.put(7)).grid(column=0,row=13,sticky=N)
        ttk.Button(mainframe,text=8, command=lambda : self.put(8)).grid(column=1,row=13,sticky=N)
        ttk.Button(mainframe,text=9, command=lambda : self.put(9)).grid(column=2,row=13,sticky=N)
        ttk.Button(mainframe,text=4, command=lambda : self.put(4)).grid(column=0,row=14,sticky=N)
        ttk.Button(mainframe,text=5, command=lambda : self.put(5)).grid(column=1,row=14,sticky=N)
        ttk.Button(mainframe,text=6, command=lambda : self.put(6)).grid(column=2,row=14,sticky=N)
        ttk.Button(mainframe,text=1, command=lambda : self.put(1)).grid(column=0,row=15,sticky=N)
        ttk.Button(mainframe,text=2, command=lambda : self.put(2)).grid(column=1,row=15,sticky=N)
        ttk.Button(mainframe,text=3, command=lambda : self.put(3)).grid(column=2,row=15,sticky=N)
        ttk.Button(mainframe,text=0, command=lambda : self.put(0)).grid(column=0,row=16,columnspan=2,sticky=(N,E,S,W))
        ttk.Button(mainframe,text='.', command=lambda: self.put('.')).grid(column=2,row=16,sticky=N)
       
               
        for key in range(10):
             root.bind(str(key),self.keypress)

        root.bind('.', self.keypress)
        root.bind('<Shift-C>',self.clear)
        root.bind('c',self.backspace)
        root.bind('%',self.percent) 
        root.bind('+',self.arithmetic_keypress) 
        root.bind('-',self.arithmetic_keypress) 
        root.bind('*',self.arithmetic_keypress) 
        root.bind('/', self.arithmetic_keypress) 
        root.bind('(', self.keypress)
        root.bind(')', self.keypress)
        root.bind('<Return>', self.equals)

 
        self.put(0)

    def keypress(self, arg):
        self.put(arg.char)
    
    def arithmetic_keypress(self, arg):
        arithmetic_symbol = {'*':'×','/':'÷', '+':'+', '-':'-'}
        self.calculate(arithmetic_symbol[arg.char])

    def equals(self, arg):
        self.calculate('=')

    def put(self,arg):
        temp = self.display.get()
        if temp == 'Not a Number':
            temp = ''

        if arg == '.' and temp == '0': 
            temp = '0'
        elif temp == '0': 
            temp = ''
        if arg == '.' and '.' in temp.split()[-1]:
            return
        elif arg == '.' and temp.split()[-1] in Calculator.operators:
            temp += '0'
        elif arg == ')' and len(re.findall(r'\)',temp)) >= len(re.findall(r'\(',temp)):
            return
        elif arg == ')' and temp[-1] == '(':
            return  
         
       

        temp += str(arg)  
        self.display.set(temp)
   
    def sign(self,arg):
        temp = self.display.get()
        if temp == '0':
            return 
        elif len(temp.split()) == 1 and temp[0] != '-':
            self.display.set('-' + temp)
        elif temp[0] == '-' and len(temp.split()) == 1:
            self.display.set(temp[1:])        
        elif len(temp.split())  != 1 and temp.split()[-1][0] == '-': 
            self.display.set(' '.join(temp.split()[:-1]) + ' ' + temp.split()[-1][1:])
        elif len(temp.split())  != 1 and temp.split()[-1][0] != '-':
            self.display.set(' '.join(temp.split()[:-1]) + ' -' + temp.split()[-1])
        elif temp.split()[-3:] == ' - ': 
            temp += ' -'
            self.display.set(temp)
        if (temp.split()[-1] in Calculator.operators ) and (temp.split()[-2] not in Calculator.operators): 
            
            temp += ' -'
            self.display.set(temp)

    def percent(self,arg):

        temp = self.display.get()
        temp2 = temp.split()[-1]

        if temp2[0] == '-': 
            sign = '-'
            temp2 = temp2[1:]
        else:
            sign = ''
        
        if temp2[0] == '.':
            temp2 ="0.00" + temp2[1:]
        elif temp2[1] == '.':
            temp2 = "0.0" + temp2.replace('.','')

        elif '.' in temp2:
            temp2 = temp2.split('.')[0][:-2] + '.' + temp2.split('.')[0][-2:] + temp2.split('.')[1] 
            if temp2[0] == '.':
                temp2 = '0' + '.' + temp2[1:]
        else: 
            temp2 = temp2[:-2] + '.' + temp2[-2:]
              
        self.display.set(' '.join(temp.split()[:-1] + [sign + temp2]))

        
    def backspace(self,arg):
        temp = self.display.get()
        if temp[0] == '-' and len(temp) == 2:
            self.display.set(0)
        elif len(temp) == 1: 
            self.display.set(0)
        else:
            if temp[-1] == ' ':
                self.display.set(temp[:-3])
            else:
                self.display.set(temp[:-1])
    
    def clear(self,arg):
        self.display.set(0)
     
    def calculate(self,operator):
        temp = self.display.get()
        
        if operator == '=':
            try:
                self.display.set(eval(re.sub('÷','/' ,re.sub(r'×','*',temp))))
            except:
                self.display.set('Not a Number')
            finally:
                return
        elif temp[-1] in ')0123456789': 
            temp += " "  + operator + " "
        elif temp[-2] in Calculator.operators:
            temp = temp[:-2] + operator + " " 
        
            
        self.display.set(temp)

    
root = Tk()
calc = Calculator(root)
root.mainloop()
