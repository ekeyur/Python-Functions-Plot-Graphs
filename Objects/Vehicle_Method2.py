class Vehicle(object):
    def __init__(this,make,model,year):
        this.make = make
        this.model = model
        this.year = year

    def print_info(this):
        print this.make, this.model, this.year

car = Vehicle('Nissan','Leaf',2015)
car.print_info()
