myDict = {}
print myDict
print

# add element
myDict['name'] = 'Pater'
print myDict
print

# initialize with entry
newDict = {'phone': '066410100200'}
print newDict
print

# update with new
myDict.update(newDict)
print myDict
print

# view values:
print myDict.keys()
print

# view values:
print myDict.values()
print

# view items
print myDict.items()
print

# delete item
del myDict['phone']
print myDict
print

# clear entire dict
myDict.clear()
print myDict
print