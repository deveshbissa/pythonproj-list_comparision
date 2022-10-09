# -----------------------------------------------------------
# demonstrates how to merge list of Tuples in Python
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------

def mergeListsOfTuples(list1,list2):
    list1_set = set(list1)
    list2_set = set(list2)
    return list(list1_set.union(list2_set))