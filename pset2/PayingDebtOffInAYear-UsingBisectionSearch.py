__author__ = 'Shivam B. Waghela'
# program executed correctly with the staff's input set.
# Uses Bisection Search to increasing the efficiency of the program.
# PayingDeftOffInAYear.py is another version of this problem, but less accurate and less efficient.

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12
unpaidBalance = balance

monthlyPayLB = balance/12.0  # Monthly payment with 0% Interest Rate
monthlyPayUB = (balance * (1 + monthlyInterestRate)**12)/12.0

monthlyPay = monthlyPayLB

while round(unpaidBalance, 2) != 0.00:  # rounding fixed the infinite loop and led to the correct answer
    if unpaidBalance > 0.00:
        monthlyPayLB = monthlyPay
    else:
        monthlyPayUB = monthlyPay    
    unpaidBalance = balance
    monthlyPay = (monthlyPayLB + monthlyPayUB)/2.0
    for i in range(1, 13):   # for each month in a year
        unpaidBalance -= monthlyPay
        unpaidBalance += round(unpaidBalance*monthlyInterestRate, 2) # Adding interest on the unpaid balance
print('Lowest payment: ' + str(round(monthlyPay, 2)))