__author__ = 'Shivam Waghela'

vowels = ['a','e','i','o','u']
s = raw_input('Enter a string: ')
count = 0
for char in s:
    if char in vowels:
        count += 1
print('Number of vowels: ' + str(count))