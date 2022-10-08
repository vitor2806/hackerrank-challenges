def ginortS(string):
    notSorted = list(string)
    notSorted.sort()
    upperList = []
    lowerList = []
    evenList = []
    oddList = []

    for char in notSorted:
      if (char.isupper()):
        upperList.append(char)
      elif (char.islower()):
        lowerList.append(char)
      elif (int(char) % 2 != 0):
        oddList.append(char)
      else:
        evenList.append(char)
    
    sortedList = ''.join(lowerList) + ''.join(upperList) + ''.join(oddList) + ''.join(evenList)
    print(sortedList)

s = input()
ginortS(s)