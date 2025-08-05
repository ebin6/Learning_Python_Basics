from abc import ABC,abstractmethod

class Parent(ABC):
    @abstractmethod
    def fun(self):
        pass

class Child(Parent):
    def Display(self):
        print("Hi")
    def fun(self):
        print("Abstract method implementation")


ob=Child()
ob.Display()
ob.fun()