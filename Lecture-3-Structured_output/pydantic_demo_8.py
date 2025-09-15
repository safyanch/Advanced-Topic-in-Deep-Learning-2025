from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Dr. M.Safyan'
    age: Optional[int] = None
    email: EmailStr 
    cgpa: float = Field(gt=0, lt=4)
    
new_student = {'age':'32', 'email':'abc@gmail.com', 'cgpa': '3'}

student = Student(**new_student)

#student_dict = dict(student)

print(student)

