__author__ = 'Shivam B. Waghela'

# define function for arbitrary radioactive decay curve
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

# calculate the amount of radiation a person is exposed to during some period of time
def radiationExposure1(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    radiationExposed = 0.0
    while (round(stop-start, 1) != 0.0):
        radiationExposed += f(start)*step
        start += step
    return radiationExposed


def radiationExposure(start, stop, step):

    radiationExposed = 0.0
    if (round(start-stop, 1) ==  0.0):
            return radiationExposed
    else:
        radiationExposed += f(start)*step
        return radiationExposed + radiationExposure(start+step, stop, step)

print radiationExposure(0, 3, 0.1)