__author__ = 'Shivam B. Waghela'

# prints the longest substring of a given string in which the letters occur in alphabetical order.

s = raw_input('Enter a string: ')
current = s[0]
longest = s[0]                        ##not longest = ''
for i in range(1, len(s)):
    if s[i] >= current[-1]:
        current = current + s[i]
    else:
        current = s[i]
    if len(current) > len(longest):  # '>' will give the first longest alphabetical substring encountered
        longest = current            # and '>=' will give the last longest alphabetical substring
print('Longest substring in alphabetical order is: ' + longest)