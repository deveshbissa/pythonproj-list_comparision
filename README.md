# pythonproj-list_comparision
This utiliy compare Two list of records.
- It provides gaps of each list. E.g. missing records of list 1 and missing records of list 2.
- It merges records of both lists and provides master list with both results.

E.g. list of records :
List of Touples :
        a = [("abc","cde"),("ver","tes"),("ber","est"),("vre","bse"),("der","fer")]
        b = [("abc","cdc"),("ver","tes"),("ber","est"),("vre","bse"),("per","lkret")]

list_1 missing following:
 [('abc', 'cdc'), ('per', 'lkret')]
list_2 missing following:
 [('der', 'fer'), ('abc', 'cde')]


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

list_1 missing following:
 [{'name': 'Jon', 'age': 24}, {'name': 'Aly', 'age': 32}, {'age': '', 'name': 'Mike'}]
list_2 missing following:
 [{'name': 'Aly', 'age': 35}, {'age': 24, 'name': 'John'}]


Refer Input.txt for sample input.
    
