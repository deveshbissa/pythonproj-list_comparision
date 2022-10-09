# -----------------------------------------------------------
# Utilities used by different modules
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------


'''
convert a list of dictionary to Frozenset
'''
def getFrozenSet(list_data):
    convert_to_tuples = lambda l: set(frozenset(d.items()) for d in l)
    return convert_to_tuples(list_data)

'''
Get data type of records inside list (Either tuple or dict)                                                   
'''
def getTypeOfList(ilist):
    return type(ilist[0]).__name__



'''
Convert a Frozenset to dictionary
'''
def fsetToList(data):
    list_master=[]
    for s in data:
        t = dict((x, y) for x, y in s)
        list_master.append(t)
    return list_master