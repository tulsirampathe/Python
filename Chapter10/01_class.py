class Employee:
    language = "Py" # this is a class attribute
    salary = 140000
    
    
pathe = Employee()
pathe.name = "Tulsiram Pathe" # this is a instance attribute
print(pathe.name, pathe.language, pathe.salary)

# Here name is instance attritute and salary and language are class attributes as they directly belong to the class