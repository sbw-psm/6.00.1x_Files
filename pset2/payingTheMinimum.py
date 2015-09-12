__author__ = 'Shivam B. Waghela'
print('Jai Swaminarayan')

balance = 50000
annualInterestRate = 0.24
monthlyPaymentRate = 0.02

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
