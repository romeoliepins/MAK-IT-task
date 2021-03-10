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
            return self.start is True, "The car has been started!"
        elif self.tank == 0:
            return "Sorry, you can't start the car, the tank is empty!"

    def stop(self):
        if self.speed == 0:
            return self.start is False, "The car has been turned off."
        elif self.speed > 0:
            return self.start is True, "You are still going, brake to stop the car!"

    def accelerate(self, speed_increase):
        if self.start:
            if self.speed + speed_increase > 100:
                return "Sorry the car goes only up a 100km/h! Try accelerating a little less."
            elif 0 < self.speed + speed_increase <= 100:
                return self.speed + speed_increase, self.tank - speed_increase * 0.1, "Your current speed is {}km/h.".format(
                    self.speed)
        else:
            return "The car hasn't been turned on!"

    def brake(self, speed_decrease):
        if self.speed == 0 and self.start is False:
            pass
        elif self.speed - speed_decrease >= 0:
            self.speed -= speed_decrease
            if self.speed > 0:
                return self.speed, "Your current speed is now {}km/h.".format(self.speed)
            elif self.speed == 0:
                return self.speed, "Your car has stopped!"
        else:
            return "Your speed decrease is too big! Try braking a little less."

    def fuel_up(self, amount):
        if self.start:
            return "You need to stop before filling the car."
        elif self.start is False:
            if self.tank + amount <= self.tank_vol:
                self.tank += amount
                if self.tank == self.tank_vol:
                    return self.tank, "The tank is full!"
                elif 0 < self.tank < self.tank_vol:
                    return self.tank, "You have {}l in your tank now".format(self.tank)
            else:
                return "Your tank is not big enough! Try filling a little less."

    def is_retro(self):
        if current_year - self.year > 25:
            return self.retro, "You have a retro car!"
        else:
            return not self.retro, "Your car needs to be at least 25 years old to qualify for a retro status."

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
