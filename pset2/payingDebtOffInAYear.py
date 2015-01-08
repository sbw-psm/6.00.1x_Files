__author__ = 'Shivam B. Waghela'

print('Jai Swaminarayan')

balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
unpaidBalance = 3329.0
monthlyPayment = 10

while unpaidBalance != 0:
    monthlyPayment *= 2
    for i in range(1, 13):
        unpaidBalance -= float(monthlyPayment)
        unpaidBalance += round(unpaidBalance*monthlyInterestRate, 2)
print('Lowest monthly payment: ' + str(monthlyPayment))