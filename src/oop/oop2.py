# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # define drive via self and return vroooom
    def drive(self):
        return "vroooom"

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"
'''
To Do:
1. write a subclass from GroundVehicle called Motorcycle
2. set the number of wheels to 2
3. google how to override a method in python - superclass
4. define the drive method
5. return "BRAAAP!!"
'''

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(num_wheels=2)
    
    def drive(self):
        return "BRAAAP!!"


'''
Overriding source & example: 
https://www.geeksforgeeks.org/method-overriding-in-python/
'''

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for v in vehicles:
    v.drive()
