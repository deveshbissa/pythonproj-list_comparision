# -----------------------------------------------------------
# demonstrates how to compare list of Tuples in Python
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------

def compareListOfTuples(list1,list2):
    list1_set = set(list1)
    list2_set = set(list2)
    list1_missing = list(list2_set.difference(list1_set))
    list2_missing = list(list1_set.difference(list2_set))
    return list1_missing , list2_missing