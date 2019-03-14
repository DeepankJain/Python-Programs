class Student:
    school_name = "KV"

    #Creating constructor for the class
    def __init__(self, name, age, standard):
        self.student_name = name
        self.student_age = age
        self.student_class = standard
    def display_details(self):
        print(self.student_name)
        print(self.student_age)
        print(self.student_class)

    def change_school_name(self, new_school_name):
        self.school_name = new_school_name


#creating object
new_student1 = Student('Deepank',16,10)

new_student1.display_details()

new_student2 = Student('Rohit',17,11)
new_student2.display_details()

new_student1.change_school_name("DPS")
print(new_student1.school_name)
