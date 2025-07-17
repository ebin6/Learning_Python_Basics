# *args

def Total(*n):
    print(sum(n))

Total(56,3,89,7)


def Greetings(**student):
    print(f"Hello {student["name"]} You are {student["age"]} years old")

Greetings(age=27,name="Ebin")