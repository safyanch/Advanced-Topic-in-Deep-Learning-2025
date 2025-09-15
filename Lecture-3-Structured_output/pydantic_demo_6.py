#default value
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    #name: str = 'Dr. M.Safyan'
    name: str 
    
#new_student={}
#new_student = {'name': 32}
new_student = {'name': 'Dr. M.Safyan'}

student = Student(**new_student)

print(type(Student))
print(student)
#print(student.name)