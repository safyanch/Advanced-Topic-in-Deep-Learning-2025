from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Dr. M.Safyan'
    age: Optional[int] = None
    email: EmailStr 
    #cgpa: float = Field(gt=0, lt=4, default=3, description='A decimal value representing the cgpa of the student')
    cgpa: float = Field(gt=0, lt=4)
new_student = {'age':'32', 'email':'abc@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)