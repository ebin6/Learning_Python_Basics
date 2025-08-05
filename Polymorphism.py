class Parent:
    def fun(self):
        print("Hi")

class Child(Parent):
    def fun(self):
        print("Child : Hello")
ob=Child()
ob.fun()