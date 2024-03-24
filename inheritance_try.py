class person():
    def __init__(fname, lname, age, gender):
        #self.fname=fname
        #self.lname=lname
        #self.age=age
        #self.gender=gender

class professor(person):
    def __init__(self,fname,lanme,salary):
        print(f"name:{self.fname} \nlast name:{self.lname} \nage:{self.age} \ngender:{self.gender} \nsalary:{salary}")

class student(person):
    def student_details(self, marks):
        print(f"name:{self.fname} \nlast name:{self.lname} \nage:{self.age} \ngender:{self.gender} \nmarks:{marks}")
    
#main
y=professor()
y.professor_details("Aditi","Mishra",19,"female",40000)

z=student()
z.student_details(93)

