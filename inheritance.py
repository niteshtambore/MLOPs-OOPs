class School:
    def __init__(self, school_name):
        self.school_name = school_name

    def get_school_details(self):
        return f"Welcome to {self.school_name}"
    
class Teacher(School):
    def __init__(self, school_name,teacher_name, subject):
        super().__init__(school_name)
        self.teacher_name = teacher_name
        self.subject = subject

    def get_teacher_details(self):
        return f"Teacher {self.teacher_name}, teaches subject {self.subject}"
    
s1 = School("H.A. School")
s2 = School("H.A. Primary School")
t1 = Teacher("H.A. School","Nitesh","Mathemetics")
t2 = Teacher("H.A. Primary School","Yogesh","Science")

print(s1.get_school_details())
print(s2.get_school_details())
print(t1.get_teacher_details())
print(t2.get_teacher_details())