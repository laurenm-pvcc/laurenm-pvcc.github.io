# Name: Lauren Magura
# Prog Purpose: This program creates a receipt for a Palermo Pizza purchase.
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

####  define global varibles  ####
# define tax rate and prices

SALES_TAX_RATE = 5.5
PR_SMALL = 9.99
PR_MEDIUM = 12.99
PR_LARGE = 14.99
PR_EXTRA_LARGE = 17.99

#### define global variables ####
global pizza_size  
num_pizzas = 0
subtotal = 0
sales_tax = 0
total = 0

#### define program functions ####
def main():
    while True:
        get_user_data()
        preform_calculations()
        display_results()
        yesno = input("\nWould you like to order another pizza? (Y/N): ")
        if yesno.upper() != "Y":
            break
    print("--------------------")
    print("--------------------")
    print("Thank you for ordering at Palermo Pizza!")
    print("--------------------")
    print("We hope to see you again soon.")
    print("--------------------")
    print
    

def get_user_data():
    global num_pizzas, pizza_size
    num_pizzas = int(input("Number of pizzas: "))
    pizza_size = input("Pizza size (S/M/L/XL): ").upper()
    

def preform_calculations():
    global subtotal, sales_tax, total
    if pizza_size == 'S':
        subtotal = num_pizzas * PR_SMALL
    elif pizza_size == 'M':
        subtotal = num_pizzas * PR_MEDIUM
    elif pizza_size == 'L':
        subtotal = num_pizzas * PR_LARGE
    elif pizza_size == 'XL':
        subotal = num_pizzas * PR_EXTRA_LARGE

    
    sales_tax = subtotal * SALES_TAX_RATE / 100
    total = subtotal + sales_tax

def display_results():
    print('----------------------')
    print('**** Palermo Pizza ****')
    print('Your neighbohood pizza place')
    print('----------------------')
    print('Pizzas       $ {:>10,.2f}'.format(subtotal))
    print('Sales Tax    $ {:>10,.2f}'.format(sales_tax))
    print('Total        $ {:>10,.2f}'.format(total))
    print('------------------------')
    print(str(datetime.datetime.now()))

#### call on main program to execute ####
main()
