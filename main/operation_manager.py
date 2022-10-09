# -----------------------------------------------------------
# Create report : compare list of Tuples/Dict in Python
# Merge Two Lists
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------
import os ,sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

from operation_util.comparision_operation import findGapsOfLists
from operation_util.merge_operation import mergeLists

def  gapInformation(list1,list2):
    list_1_miss, list_2_miss = findGapsOfLists(list1,list2)  # type: ignore
    list1_size = len(list1)
    list2_size = len(list2)
    list1_miss_count = len(list_1_miss)
    list2_miss_count = len(list_2_miss)
    print("\n============================================================\n")
    print (f"Size Of list_1 = {list1_size}")
    print (f"Size Of list_2 = {list2_size}")
    print("\n============================================================\n")
    print(f"list_1 missing following:\n {list_1_miss}")
    print(f"\nTotal missing = {list1_miss_count}\n")
    print("\n============================================================\n")
    print(f"list_2 missing following:\n {list_2_miss}")
    print(f"\nTotal missing = {list2_miss_count}\n")
    
    
    
def mergeOpsLists(list1,list2):
    master_list = mergeLists(list1,list2)
    print("================After Merge ==========================\n")
    master_list_size = len(master_list)
    print(master_list)
    print (f"\nSize Of master_list = {master_list_size}")
    print("\n============================================================\n")