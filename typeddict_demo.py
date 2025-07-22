from typing import TypedDict

class person(TypedDict):
    
    name: str
    age: int

new_person: person = {'name': 'uneiz', 'age':'twenty-four'} 

print(new_person)