# Change Calculator. 

# Idea 1: Simple structures for programming, no paragdims: OOP. 
# Modules: Used.
# Program Structure: Main function and helper functions. 
# Paradgim: Procedural. 
# Monetary System Used: Australian, Current.
# Other Information: Gives fewest bills and coins. 
# TO DO: Testing, Algo DS, Sys Design etc.. 

from math import ceil
def change_to_use(change):
    change2 = round((change // 1) + ceil(round(change % 1,2) / 0.05) * 0.05,2)
    return change2

def make_change():
    while True:
        print (" ------ Change Calculator, Currency System: Australian -------- ")
        try:
            charged_amount, paid_amount = float(input('\nAmount Charged: ')), float(input('Amount Paid: '))
            change  = round(paid_amount - charged_amount,2)
            
            aus_currency_2023 = [5, 10, 20, 50, 100, 0.05, 0.10, 0.20, 0.50, 1, 2]
            aus_currency_2023.sort() 

            if paid_amount < charged_amount:
                print ("Charge not paid fully, please ensure full payment occurs.")
                raise

            if charged_amount < 0 or paid_amount < 0: 
                print("Currency can't be negative !")
                raise

            max_curr_applicable = None

            change2 = change_to_use(change)           

            print('Change To Give:', change)

            if change != change2: 
                print("Actual Change Given (Due to Currency Coins):", change2)
                print("Extra amount Given:", round(change2 - change,2))

            print('Notes/Coins to give back:')
            while change2 > 0:
                
                for currency in aus_currency_2023:
                    if currency > change2:
                        break
                    max_curr_applicable = currency
             
                print(max_curr_applicable)
                change2 -= max_curr_applicable
                
                if type(change2) is float: 
                    change2 = round(change2,2)

        except ValueError:
            print('Ensure Only Currency (float or integer) is Entered')
            
    





if __name__ == '__main__':
    make_change()








