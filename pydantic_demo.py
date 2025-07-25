from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'uneiz'
    age: Optional[int] = None
    email: EmailStr
    cgpa : float = Field(gt=0, lt=10, description="A decimal value representing the CGPA of the student")

new_student = {'age':24, 'email': 'abc@gmail.com', 'cgpa': 5}


student = Student(**new_student)

student_dict = dict(student)

student_json = student.model_dump_json()

print(student)
print(student_dict)
print(student_json)
