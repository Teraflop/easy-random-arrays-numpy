import numpy as np

def create1DArray(size, mag):
    '''
    Create a random, uniformly distributed 1d numpy array of
    the specified size consisting of only natural numbers
    with the number of places as specified by mag
    '''
    #check for invalid parameters
    if size <= 0 or mag == 0 or not isinstance(size, int)or not isinstance(mag, int):
        return None
    #create the numpy array
    name = np.random.random(size)

    #iterate through each number to round it
    for place, num in enumerate(name):
        #this can be changed depending on the order of magnitude of your numbers
        num *= mag * 10
        #round to zero decimal places
        num = num.round(0)
        #replace the old decimal with the new integer
        name[place] = num
    return name

def createNormal1DArray(size, mag):
    '''
    Create a random, normally distributed 1d numpy array of
    the specified size consisting of only natural numbers
    with the number of places as specified by mag
    '''
    #check for invalid parameters
    if size <= 0 or mag == 0 or not isinstance(size, int)or not isinstance(mag, int):
        return None

    #create the numpy array
    name = np.random.randn(size)

    #iterate through each number to round it
    for place, num in enumerate(name):
        #this can be changed depending on the order of magnitude of your numbers
        num *= mag * 10
        #round to zero decimal places
        num = num.round(0)
        #replace the old decimal with the new integer
        name[place] = num
    return name

def createMatrix(width, height, mag):
    '''
    Create a random, uniformly distributed 2d numpy array of
    the specified dimensions consisting of only natural numbers
    with the number of places as specified by mag
    '''
    #check if any parameters are invalid
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(mag, int) or width <= 0 or height <= 0 or mag == 0:
        return None
    #create the numpy array
    name = np.random.random((height, width))
    #iterate through the columns to yield a row
    for p, i in enumerate(name):
        #iterate through each row
        for place, number in enumerate(name[p]):
            #can be changed depending on the order of magnitude of your numbers
            number *= mag * 10
            #round to zero decimal places
            number = number.round(0)
            #replace the old decimal with the new integer
            i[place] = number
    return name

def createNormalMatrix(width, height, mag):
    '''
    Create a random, normally distributed 2d numpy array of
    the specified dimensions consisting of only natural numbers
    with the number of places as specified by mag
    '''
    #check if any parameters are invalid
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(mag, int) or width <= 0 or height <= 0 or mag == 0:
        return None

    #create the numpy array
    name = np.random.randn(height, width)
    #iterate through the columns to yield a row
    for p, i in enumerate(name):
        #iterate through each row
        for place, number in enumerate(name[p]):
            #can be changed depending on the order of magnitude of your numbers
            number *= mag * 10
            #round to zero decimal places
            number = number.round(0)
            #replace the old decimal with the new integer
            i[place] = number
    return name
