def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    i = 0
    result = 0
    while i < len(listA):
        result += listA[i] * listB[i]
        i += 1
    return result

print dotProduct([1, 2, 3], [4, 5, 6])