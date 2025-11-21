class Teacher:
    def __init__(self):
        self.__id = "1001"      # -> hiding an attribute using __id, Attributes with double underscores __ are treated as private.
        self.name = "nitesh"
        self.experience = "10yrs"

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if len(new_id) == 4:
            self.__id = new_id
        else:
            return "please enter a valid id"

new_teacher = Teacher()

try:
    print(new_teacher.id)           # -> AttributeError: 'Teacher' object has no attribute 'id'
except:
    pass

new_teacher.subject = "mathematics"

print(new_teacher.subject)

print(new_teacher.get_id())         # -> mathematics

new_teacher.set_id("1002")          # -> 1001
print(new_teacher.get_id())         # -> 1002