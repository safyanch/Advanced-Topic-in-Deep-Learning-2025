# optional  value
# type converstion
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):

    name: str = 'Dr. Atif Kamal'
    age: Optional[int]=None
new_student = {'age': 45}
#new_student = {}
#new_student = {'age': '45'}
student = Student(**new_student)

print(student)
print(student.name)