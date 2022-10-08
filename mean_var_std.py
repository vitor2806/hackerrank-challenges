import numpy

n, m = list(map(int, input().split()))
holdingList = numpy.array([list(map(int, input().split())) for element in range(n)])
    
print(numpy.mean(holdingList, axis=1))
print(numpy.var(holdingList, axis=0))
print(round(numpy.std(holdingList), 11))