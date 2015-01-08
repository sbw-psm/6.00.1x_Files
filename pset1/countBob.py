__author__ = 'Shivam B. Waghela'

# Counts number of 'bob' in a given string

s = raw_input('Enter a string: ')
BobCount = 0
for i in range(len(s) + 1):
    if s[i:i + 3] == 'bob':
        BobCount += 1
print('Number of times bob occurs is: ' + str(BobCount))