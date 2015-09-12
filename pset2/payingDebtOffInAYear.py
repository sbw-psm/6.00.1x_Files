__author__ = 'Shivam B. Waghela'
# Program working properly as per the test inputs.
# Not accurate in calculating monthly payment 
# As the program calculates monthly payment as a multiple of 10.
# And it can be slower where the balance amount is very large(eg.: 3400000).
# More accurate solution: PayingDebtOffInAYear-UsingBisectionSearch.py.

balance = 50000
annualInterestRate = 0.24

monthlyInterestRate = annualInterestRate/12
unpaidBalance = balance
monthlyPayment = 0

while unpaidBalance > 0:     # while the debt is not paid off in year
    unpaidBalance = balance
    monthlyPayment += 10      # Increasing the monthlyPayment by the multiple of 10
    for i in range(1, 13):   # for each month in a year
        unpaidBalance -= monthlyPayment 
        unpaidBalance += round(unpaidBalance*monthlyInterestRate, 2) # Adding interest on the unpaid balance
print('Lowest payment: ' + str(monthlyPayment))

