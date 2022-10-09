# -----------------------------------------------------------
# demonstrates how to merge list of dictionary in Python
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------


from common_util import common_ops as co

def mergeListsOfDict(list1,list2):
    list1_fset = co.getFrozenSet(list1)
    list2_fset = co.getFrozenSet(list2)
    res = list(list1_fset.union(list2_fset))
    list_master=[]
    for s in res:
        t = dict((x, y) for x, y in s)
        list_master.append(t)
    return list_master