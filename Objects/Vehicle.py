class Vehicle(object):
    def __init__(this,make,model,year):
        this.make = make
        this.model = model
        this.year = year

car = Vehicle('Nissan','Leaf',2015)
print car.make, car.model, car.year
