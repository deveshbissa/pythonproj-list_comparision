# pythonproj-list_comparision
This utiliy compare Two list of records.
- It provides gaps of each list. E.g. missing records of list 1 and missing records of list 2.
- It merges records of both lists and provides master list with both results.

E.g. list of records :

- List of Touples :
        a = [("abc","cde"),("ver","tes"),("ber","est"),("vre","bse"),("der","fer")]
        b = [("abc","cdc"),("ver","tes"),("ber","est"),("vre","bse"),("per","lkret")]

-output 

list1 = [('abc', 'cde'), ('ver', 'tes'), ('ber', 'est'), ('vre', 'bse'), ('der', 'fer')]

list2 = [('abc', 'cdc'), ('ver', 'tes'), ('ber', 'est'), ('vre', 'bse'), ('per', 'lkret')]


============================================================

Size Of list_1 = 5
Size Of list_2 = 5

============================================================

list_1 missing following:
 [('abc', 'cdc'), ('per', 'lkret')]

Total missing = 2


============================================================

list_2 missing following:
 [('abc', 'cde'), ('der', 'fer')]

Total missing = 2

================After Merge ==========================

[('ver', 'tes'), ('vre', 'bse'), ('abc', 'cdc'), ('der', 'fer'), ('per', 'lkret'), ('abc', 'cde'), ('ber', 'est')]

Size Of master_list = 7

============================================================


List of dictionary:

    list_1 = [
        { 'name': 'Miken', 'age': 40},
        { 'name': 'Johnn', 'age': 24},
        { 'name': 'Alyn', 'age': 35}
    ]

    list_2 = [
        { 'name': 'Miken', 'age':40 },
        { 'name': 'Jonn', 'age': 24},
        { 'name': 'Alyn', 'age': 32},
        { 'name': 'Allyn', 'age': 44}]

Output:

list1 = [{'name': 'Miken', 'age': 40}, {'name': 'Johnn', 'age': 24}, {'name': 'Alyn', 'age': 35}]

list2 = [{'name': 'Miken', 'age': 40}, {'name': 'Jonn', 'age': 24}, {'name': 'Alyn', 'age': 32}, {'name': 'Allyn', 'age': 44}]


============================================================

Size Of list_1 = 3
Size Of list_2 = 4

============================================================

list_1 missing following:
 [{'name': 'Jonn', 'age': 24}, {'age': 32, 'name': 'Alyn'}, {'age': 44, 'name': 'Allyn'}]

Total missing = 3


============================================================

list_2 missing following:
 [{'name': 'Johnn', 'age': 24}, {'name': 'Alyn', 'age': 35}]

Total missing = 2

================After Merge ==========================

[{'age': 40, 'name': 'Miken'}, {'age': 32, 'name': 'Alyn'}, {'name': 'Johnn', 'age': 24}, {'age': 44, 'name': 'Allyn'}, {'name': 'Jonn', 'age': 24}, {'name': 'Alyn', 'age': 35}]

Size Of master_list = 6

============================================================




Refer Input.txt for sample input.
    
