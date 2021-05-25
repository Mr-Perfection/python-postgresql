class Student:
    def __init__(self, name, courses = []): # bad idea
        self.name = name
        self.courses = courses
    def add_course(self, course):
        self.courses.append(course)
    
hello = Student("hello")
olah = Student("olah")
hello.add_course("kool")
olah.add_course("yolo")

print(hello.courses)
print(olah.courses) # has ['kool'] as well because class initializes courses as an mutable object inside the class.
# hello.add_course("kool")

from typing import Optional, List

class Student:
    def __init__(self, name: str, courses: Optional[List[str]] = None): 
        self.name = name
        self.courses = courses or []
    def add_course(self, course: str):
        self.courses.append(course)
hello = Student("hello")
olah = Student("olah")
hello.add_course("kool")
olah.add_course("yolo")

print(hello.courses)
print(olah.courses)