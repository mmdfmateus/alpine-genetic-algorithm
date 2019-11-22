

def calculateMax(vec):
    max = vec[0][2]
    maxIndex = 0
    for index, v in enumerate(vec):
        if (v[2] > max):
            max = v[2]
            maxIndex = index
    return maxIndex


def calculateMin(vec):
    min = vec[0][2]
    minIndex = 0
    for index, v in enumerate(vec):
        if (v[2] < min):
            min = v[2]
            minIndex = index
    return minIndex

def calculateMed(vec, size):
    return (vec[size-1][3])/size
