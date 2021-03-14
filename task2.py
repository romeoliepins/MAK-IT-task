from datetime import date

current_year = date.today().year


class Car:
    def __init__(self, model, year, tank_vol):
        self.model = model
        self.year = year
        self.tank_vol = tank_vol
        self.start = False
        self.speed = 0
        self.tank = 0
        self.retro = False

    def start_up(self):
        if self.tank > 0:
            self.start = True
            print("The car has been started!")
            return True
        elif self.tank == 0:
            self.start = False
            print("Sorry, you can't start the car, the tank is empty!")
            return False

    def stop(self):
        if self.speed == 0:
            self.start = False
            print("The car has been turned off.")
            return False
        elif self.speed > 0:
            self.start = True
            print("You are still going, brake to stop the car!")
            return True

    def accelerate(self, speed_increase):
        if self.start:
            if self.speed + speed_increase > 100:
                print("Sorry the car goes only up a 100km/h! Try accelerating a little less.")
                return False
            elif 0 < self.speed + speed_increase <= 100:
                self.speed += speed_increase
                self.tank - speed_increase * 0.1
                print("Your current speed is {}km/h.".format(
                    self.speed))
                return self.speed
        else:
            print("You need to start the car!")
            return False

    def brake(self, speed_decrease):
        if self.speed == 0:
            print("The car has stopped, you can't brake!")
            return False
        elif self.start is False:
            print("The car is turned off, you can't brake!")
            return False
        elif self.speed - speed_decrease >= 0:
            self.speed -= speed_decrease
            if self.speed > 0:
                print("Your current speed is now {}km/h.".format(self.speed))
                return self.speed
            elif self.speed == 0:
                print("Your car has stopped!")
                return self.speed
        elif self.speed - speed_decrease <= 0:
            print("Your speed decrease is too big! Try braking a little less.")
            return False

    def fuel_up(self, amount):
        if self.start:
            print("You need to stop before filling the car.")
            return False
        elif self.start is False:
            if self.tank + amount <= self.tank_vol:
                self.tank += amount
                if self.tank == self.tank_vol:
                    print("The tank is full!")
                    return self.tank
                elif 0 < self.tank < self.tank_vol:
                    print("You have {}l in your tank now".format(self.tank))
                    return self.tank
            else:
                print("Your tank is not big enough! Try filling a little less.")
                return False

    def is_retro(self):
        if current_year - self.year > 25:
            self.retro = True
            print("You have a retro car!")
            return True
        else:
            self.retro = False
            print("Your car needs to be at least 25 years old to qualify for a retro status.")
            return False

    def __str__(self):
        return str(self.model), str(self.year)


my_car = Car("A3", 2020, 50)
print(my_car.is_retro())
print(my_car.start_up())
print(my_car.accelerate(50))
print(my_car.fuel_up(60))
print(my_car.fuel_up(50))
print(my_car.start_up())
print(my_car.accelerate(110))
print(my_car.accelerate(50))
print(my_car.tank)
print(my_car.brake(25))
print(my_car.stop())
print(my_car.brake(25))
print(my_car.stop())
print(my_car.__str__())
