class employee:
    def __init__(self): # special / magical method / dunder method - constructor
        print("why it is called constructor, please run the code and understand")
        print("Started executing attributes -> nitesh = employee()")
        self.id = 1001
        self.salary = 20000
        self.designation = "Software Engineer"
        print("Attributes initiated")
        print("We can see that only attributes got invoked when we created a object of employee, any function didnot invoke, as we know functions only get invoked when we call then explicitly")

    def travel(self, id, destination): # is called method when we define it in class
        print("""started calling method explicitly -> nitesh.travel(1002, "Pune")""")
        print("Employee id ",id, "is travelling to ", destination)
        print("method calling completed")

nitesh = employee() # creating a object of class employee

# print("id ",nitesh.id,"\nsalary ",nitesh.salary,"\ndesignation ",nitesh.designation)
    
nitesh.travel(1002, "Pune")