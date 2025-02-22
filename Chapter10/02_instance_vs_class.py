class Employee:
    language = "Py" # this is a class attribute
    salary = 140000
    
    
pathe = Employee()
pathe.language = "JavaScript" # this is a instance attribute
print(pathe.language, pathe.salary)

