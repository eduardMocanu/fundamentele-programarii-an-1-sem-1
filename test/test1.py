class Person:

    def __init__(self):
        self.nume = "Edy"
        self.age = 2


    def __str__(self):
        return "{nume:" + self.nume + "}"


persoana = Person()
print(persoana)