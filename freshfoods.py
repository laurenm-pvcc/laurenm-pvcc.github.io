# Name: Lauren Magura
# Prog purpose is to calculate Fresh Food employee's weekly gross pay, deductions, 
# and net pay for an employee based on the number of hours they worked and their job category.


import datetime

# define hourly pay rates
CASHIER_RATE = 16.50
STOCKER_RATE = 15.75
JANITOR_RATE = 15.75
MAINTENANCE_RATE = 19.50

# define job categories
JOB_CATEGORIES = (
    ('C', 'c', 'CASHIER_RATE', 'Cashier',),
    ('S', 's', 'Stocker', 'STOCKER_RATE',),
    ('J', 'j', 'Janitor', 'JANITOR_RATE',),
    ('M', 'm', 'Maintenance', 'MAINTENANCE_RATE',),
)

# define deductions
FEDERAL_TAX = 0.12
STATE_TAX = 0.03
SS_TAX = 0.062
MEDICARE_TAX = 0.0145

#define deductions
DEDUCTION_RATES = (
    ('FEDERAL_TAX',),
    ('STATE_TAX',),
    ('SS_TAX',),
    ('MEDICARE_TAX',),
)

def main():
    while True:
        # get user data
        job_category_code = input("Enter job category code (C, S, J, or M): ")
        num_hours = float(input("Enter number of hours worked: "))

        # define hourly pay rate based on job category code
        if job_category_code.upper() == "C":
            hourly_pay_rate = CASHIER_RATE
        elif job_category_code.upper() == "S":
            hourly_pay_rate = STOCKER_RATE
        elif job_category_code.upper() == "J":
            hourly_pay_rate = JANITOR_RATE
        elif job_category_code.upper() == "M":
            hourly_pay_rate = MAINTENANCE_RATE
        else:
            print("Invalid job category code")
            continue

        # Calculate gross pay, each deduction amount, total deductions, and net pay
        gross_pay = num_hours * hourly_pay_rate
        federal_tax_deduction = gross_pay * FEDERAL_TAX
        state_tax_deduction = gross_pay * STATE_TAX
        social_security_deduction = gross_pay * SS_TAX
        medicare_deduction = gross_pay * MEDICARE_TAX
        total_deductions = federal_tax_deduction + state_tax_deduction + social_security_deduction + medicare_deduction
        net_pay = gross_pay - total_deductions

        # Print output
        print("Fresh Food Marketplace Store Employee Weekly Pay")
        print("Hours worked:               {:>8.2f}".format(num_hours))
        print("Gross Pay:                 ${:>8.2f}".format(gross_pay))
        print("Federal Tax Deduction:     ${:>8.2f}".format(federal_tax_deduction))
        print("State Tax Deduction:       ${:>8.2f}".format(state_tax_deduction))
        print("Social Security Deduction: ${:>8.2f}".format(social_security_deduction))
        print("Medicare Deduction:        ${:>8.2f}".format(medicare_deduction))
        print("Total Deductions:          ${:>8.2f}".format(total_deductions))
        print("Net Pay:                   ${:>8.2f}".format(net_pay))
        print(str(datetime.datetime.now()))
        print("-------------------------------------------------")

        response = input("Would you like to calculate another employee's hours? (Y/N): ")
        if response.upper() != "Y":
            break

    print("Thank you for using this program.")

    def main():

        print("---------------------------")

    another_question = True
    while another_question:
        answer = ()

        
        print("--------")
        question = input("\n")
        print(answer)
        print("----------------------------")

        askAgain = input("\nWould you like to calculate more hours?")
        print("-------------------------------------")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

    print("\n------------------------------")
    print("Thank you for using this program.")

main()
