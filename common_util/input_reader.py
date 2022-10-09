import ast
from warnings import catch_warnings

def getInputLists(input_file):
    count =0
    list_1=[]
    list_2=[]
    try:
        with open(input_file) as f:
            for content in f:
                if content.startswith("list"):
                    count+=1
                    content = content.strip()
                    data = content.split("=")
                    data_list = ast.literal_eval(data[1].strip())
                    if count == 1 :
                        list_1 = data_list
                    if count == 2 :
                        list_2 = data_list
                        return list_1,list_2
            if count == 0 or count <2 :
                raise Exception("Input is not avaialble please add two lists")
    except  FileNotFoundError as e:
        print(f"Error::{e}")
    except IOError as e:
        print(f"Error::{e}")
    except Exception as e:
        print(f"Error::{e}")
        
        