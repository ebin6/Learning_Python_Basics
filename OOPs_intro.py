class Laptops:
    owner="OneTeam"
    def __init__(self,r,m):
        self.RAM = r
        self.model = m

    def Spec(self,r,m):
        pass

lap1=Laptops("16 GB","Accer")
lap2=Laptops("4GB","Dell")

print(lap1.RAM)
print(lap2.RAM)

print(Laptops.owner)