# -----------------------------------------------------------
# demonstrates how to compare list of Tuples/Dict in Python
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------

from comparision_util import compare_dict as co_dict, compare_tuples as co_tuple


process_list_gaps ={
                "dict":co_dict.compareListOfDict,
                "tuple":co_tuple.compareListOfTuples
                }


def findGapsOfLists(list1:list,list2:list):
    list1_type = co_dict.co.getTypeOfList(list1)
    list2_type = co_dict.co.getTypeOfList(list2)
    
    if list1_type != list2_type:
        raise Exception(f"Different Type of Lists \n {list1_type} != {list2_type}, Make sure both lists are of same type ")
                        
    return process_list_gaps.get(list1_type)(list1,list2)
    

