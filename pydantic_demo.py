from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    
    name: str = 'uneiz'
    age: Optional[int] = None
    email: EmailStr

new_student = {'age': '24', 'email': 'abc@gmail.com'}

student = Student(**new_student)

print(student)
