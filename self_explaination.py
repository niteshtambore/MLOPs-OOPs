class Student:
    def __init__(self):
        print(id(self))                             # -> 2400871551696
        print("started initializing constructor")
        self.name = "nitesh"
        self.standard = "10th"
        print("constructer initialization completed",self.name, self.standard) 

nitesh = Student()

print(id(nitesh))                                    # -> 2400871551696 as we see, memory address of self and nitesh is same, 
                                                     # -> that means the object is only allowed to access all the attributes
                                                     # -> that means your object is only self

yogesh = Student()

yogesh.marks = "95/100"                             # -> we can create attribute to a class externally also like this2

print(yogesh.marks)