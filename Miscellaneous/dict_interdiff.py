def f(a, b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    diff = d1.viewkeys() ^ d2
    intersect = d1.viewkeys() & d2
    a = {k: f(d1[k], d2[k]) for k in intersect}
    b = {k: d1[k] for k in diff & d1.viewkeys()}
    b.update({k: d2[k] for k in diff & d2.viewkeys()})
    return a, b

#d1 = {1: 30, 2: 20, 3: 30, 5: 80}
#d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}
d1 = {1: 30, 2: 20, 3: 30}
d2 = {1: 40, 2: 50, 3: 60}
print dict_interdiff(d1, d2)