__author__ = 'Shivam Waghela'

s = raw_input('Enter a string: ')
vowels = ['a','e','i','o','u']
count = 0
for char in s:
    if char in vowels:
        count += 1
print('Number of vowels: ' + str(count))
