class School:
    school_name = "H.A. School"                 # static attribute (shared by all)
    __school_count = 1001                       # private static attribute

    def __init__(self, name):
        self.count = School.__school_count      # instance attribute
        School.__school_count += 1
        self.student_name = name                  # increment count for next student

s1 = School("Nitesh")
s2 = School("Yogesh")

print("student 1 : ", s1.school_name, s1.student_name, s1.count)
print("student 2 : ", s2.school_name, s2.student_name, s2.count)


class ResultHelper:
    
    @staticmethod
    def calculate_percentage(total_marks, max_marks):
        return (total_marks / max_marks) * 100
    
    @staticmethod
    def get_grade(percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 75:
            return "A"
        elif percentage > 60:
            return "B"
        elif percentage >= 55:
            return "C"
        else:
            return "Fail"
        
class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.student_percentage = ResultHelper.calculate_percentage(marks, 500)
        self.grade = ResultHelper.get_grade(self.student_percentage)

s1 = Student(1001, "nitesh", 450)
s2 = Student(1003, "yogesh", 475)
s3 = Student(1004, "pooja", 440)

print("s1 ",s1.id, s1.name, s1.student_percentage, s1.grade)
print("s2 ",s2.id, s2.name, s2.student_percentage, s2.grade)
print("s3 ",s3.id, s3.name, s3.student_percentage, s3.grade)