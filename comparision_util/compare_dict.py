
# -----------------------------------------------------------
# demonstrates how to compare list of dictionary in Python
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------

from common_util import common_ops as co


def compareListOfDict(list1,list2):
    list1_fset =co.getFrozenSet(list1)
    list2_fset = co.getFrozenSet(list2)
    list1_missing = list(list2_fset.difference(list1_fset))
    list2_missing = list(list1_fset.difference(list2_fset))
    return co.fsetToList(list1_missing) , co.fsetToList(list2_missing)