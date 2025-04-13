from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int
# 3 types of struc out put , below is of 1st type typeDict
# typeDict give you hint while typing that pair against a key is of which type 
student: Person = {'name':'str','age':12}
print(student)