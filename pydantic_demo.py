from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'uneiz'
    age: Optional[int] = None
    email: EmailStr
    cgpa : float = Field(gt=0, lt=10)

new_student = {'age':24, 'email': 'abc@gmail.com', 'cgpa': 5}


student = Student(**new_student)

print(student.name)
print(student.age)
print(student.email)
print(student.cgpa)
