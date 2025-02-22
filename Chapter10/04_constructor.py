class Employee:
    language = "Python" # this is a class attribute
    salary = 140000
    
    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")
    
pathe = Employee("Pathe", 150000, "JavaScript")

# pathe.name = "Pathe"

print(pathe.name, pathe.language,  pathe.salary)

