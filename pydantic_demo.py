from pydantic import BaseModel

class Student(BaseModel):
    
    name: str = 'uneiz'

new_student = {}

student = Student(**new_student)

print(student)
