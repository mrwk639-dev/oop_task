from random import randint
class Employee:
    def __init__(self, name, family, manager=None):
        self._name = name
        self._id = randint(1000, 9999)
        self._family = family
        self._manager = manager
        self.salary = 2500
    @property
    def id(self)->int:
        return self._id
    @property
    def family(self)-> dict:
        return self._family
    @property
    def apply_raise(self,employe, raise_percent: int):
        if employe._manager is not self:
            return False
        else:
            employe.salary=employe.salary * (1 + raise_percent / 100)
            print("new Salary:",employe.salary)
            return True
boss = Employee("John", {"mother": "Eve", "father": "Adam"})
emp1 = Employee("Jane", {"mother": "Alice", "father": "Bob"}, boss)
stranger = Employee("not a boss", {})
print(emp1.family)
boss.apply_raise(emp1, 10) 
