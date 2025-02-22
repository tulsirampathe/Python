class Employee:
    language = "Python" # this is a class attribute
    salary = 140000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")
    
pathe = Employee()
pathe.language = "JavaScript"


pathe.greet()
pathe.getInfo()

