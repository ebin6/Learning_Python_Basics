class Vehicles:
    def __init__(self,m,model):
        self.make=m
        self.model=model

class Car(Vehicles):
    def __init__(self,c,p,m,model):
        self.color=c
        self.power=p
        super().__init__(m,model)


c1=Car("Red","151 Bhp","2006","Kia Seltos")



print(c1.make,c1.color)