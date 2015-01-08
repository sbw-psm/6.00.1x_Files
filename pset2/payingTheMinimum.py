__author__ = 'Shivam B. Waghela'
print('Jai Swaminarayan')

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0.0

for i in range(1, 13):
    monthlyPayment = balance*monthlyPaymentRate
    balance -= monthlyPayment
    balance += balance*(annualInterestRate/12.0)
    totalPaid += monthlyPayment
    print('Month: ' + str(i))
    print('Minimum monthly payment: ' + str(round(monthlyPayment, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))
print('Total Paid: ' + str(round(totalPaid, 2)))
print('Remaining balance: ' + str(round(balance, 2)))