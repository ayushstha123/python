#A Class is like an object constructor, or a "blueprint" for creating objects.


class Vehicle:
    def __init__(self,make,model): #In the __init__ method, self refers to the instance of the class being created (obj in this case). It allows you to set the value of the instance variable for that particular instance.
        self.make=make
        self.model=model
        
    def moves(self):
        print(self.model+" is moving")
        print("Moves along....")
    
    def get_make_model(self):
        print(f" I'm a {self.make} {self.model}.")

my_car=Vehicle('Tesla','Model 3') #calling an object
# print(my_car.make)
# print(my_car.model)

my_car.get_make_model()
my_car.moves()

your_car=Vehicle("Cadillac","Escalade")
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make,model, faa_id):
        super().__init__(make,model) #borrwing from the parent
        self.faa_id=faa_id

    def moves(self):
        print("Flies along")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass

cessna=Airplane("Cessna","Skyhawk","10001")
mack=Truck("MAck","Tata mack")
Golfwagon=GolfCart("Yamaha","GC100")

cessna.get_make_model()
print(cessna.faa_id)
cessna.moves()

mack.get_make_model()
mack.moves()

Golfwagon.get_make_model()
Golfwagon.moves()



print('\n\n\n\n\n\n')
#polymorphism
#polymorphism is the ability to behave differently in respones to the same input messages
#Polymorphism, in the context of object-oriented programming (OOP), refers to the ability of different classes to be treated as objects of a common superclass. It allows objects of different classes to be used interchangeably based on their common interface or behavior.

for v in (my_car,your_car,cessna,mack,Golfwagon):
    v.get_make_model()
    v.moves()


