class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        

p = Programmer("Tulsiram", 100000, 480111)

print(p.name, p.company, p.salary, p.pin)