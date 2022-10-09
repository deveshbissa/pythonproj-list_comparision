# -----------------------------------------------------------
# demonstrates how to merge list of Tuples/Dict in Python
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------

from merge_util import merge_list_dict as mg_dict, merge_list_tuples as mg_tuple





process_list_merge = {
                "dict":mg_dict.mergeListsOfDict,
                "tuple":mg_tuple.mergeListsOfTuples
                }


def mergeLists(list1,list2):
    list1_type =mg_dict.co.getTypeOfList(list1)
    list2_type = mg_dict.co.getTypeOfList(list2)
    
    if list1_type != list2_type:
        raise Exception(f"Different Type of Lists \n {list1_type} != {list2_type}, Make sure both lists are of same type ")
                        
    return process_list_merge.get(list1_type)(list1,list2)