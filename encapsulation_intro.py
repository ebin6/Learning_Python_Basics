"""
Private
class Employee:
    def __init__(self):
        self.__name="Ebin"
        self.age=27

    def Display(self):
        print(self.__name,self.age)

ob=Employee()

ob.Display()
print(ob.__name)
"""
# Protected

class Parent:
    def __init__(self):
        self._name="Ebin"
    def Display(self):
        print("Name : ",self._name)

class Child(Parent):
    def ShowDetail(self):
        print(self._name)

c=Child()
c.Display()
c.ShowDetail()

print(c._name)