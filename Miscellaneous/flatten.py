#from compiler.ast import flatten

import collections
def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if isinstance(aList, collections.Iterable):
        return [a for i in aList for a in flatten(i)]
    else:
        return [aList]
print flatten([1, [ [2, 3], 4, [5, 6]], 7])