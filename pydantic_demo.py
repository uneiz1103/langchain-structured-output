from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    
    name: str = 'uneiz'
    age: Optional[int] = None

new_student = {'age': 24}

student = Student(**new_student)

print(student)
