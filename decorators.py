

"""def Substract(a,b):
    print(a-b)


Substract(45,50)

"""
def Dec(fun):
    def nested_fun(message):
        a=message.upper()

        fun(a)
    return nested_fun

@Dec
def Greetings(m):
    print(m)
Greetings("Hello Developers")
