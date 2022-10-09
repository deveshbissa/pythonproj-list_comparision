# -----------------------------------------------------------
# compare list of Tuples/Dict in Python and
# Merge Two Lists
# Author : Devesh Bissa
# email deveshbissa.rediff@gmail.com
# -----------------------------------------------------------
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

from common_util.input_reader import getInputLists  
from operation_manager import gapInformation,mergeOpsLists

def main():
    input_file = os.path.join(current_dir,"input.txt")

    list1,list2 = getInputLists(input_file)  # type: ignore

    print(f"list1 = {list1}\n")
    print(f"list2 = {list2}\n")

    gapInformation(list1,list2)
    mergeOpsLists(list1,list2)
    
    
if __name__ == '__main__':
    main()


