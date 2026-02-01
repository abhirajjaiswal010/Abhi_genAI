class employee:
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        print(self.name,self.salary,employee.company)

class developer(employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language
    def write_code(self):
        print(self.name,"writes code in ",self.language)

class manager(employee):
    def __init__(self, name, salary, teamSize):
        super().__init__(name, salary)
        self.teamSize = teamSize

    def conductMeeting(self):
        print(self.name, "conducts meeting for", self.teamSize, "members")

dev1 = developer("Abhi", 60000, "Python")
dev1.get_details()
mgr1 = manager("Rahul", 90000, 10)
mgr1.get_details()
