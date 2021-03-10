from datetime import date

current_year = date.today().year


class Car:
    def __init__(self, model, year, tank_vol, start=False, speed=0, tank=0, retro=False):
        self.model = model
        self.year = year
        self.tank_vol = tank_vol
        self.start = start
        self.speed = speed
        self.tank = tank
        self.retro = retro

    def start_up(self):
        if self.tank > 0:
            self.start = True
            print("The car has been started!")
        elif self.start is False:
            print("Sorry, you can't start the car, the tank is empty!")
        # elif self.tank_vol > 0:
        #     self.start = True

    def stop(self):
        if self.speed == 0:
            self.start = False
            print("The car has been turned off.")
        elif self.speed > 0:
            self.start = True
            print("You are still going, brake to stop the car!")

    def accelerate(self, speed_increase):
        if self.start:
            if self.speed + speed_increase > 100:
                print("Sorry the car goes only up a 100km/h! Try accelerating a little less.")
            elif 0 < self.speed + speed_increase <= 100:
                self.speed += speed_increase
                self.tank -= speed_increase * 0.1
                print("Your current speed is {}km/h.".format(self.speed))
        else:
            print("The car hasn't been turned on!")

    def brake(self, speed_decrease):
        if self.speed == 0 or self.start is False:
            pass
        elif self.speed - speed_decrease >= 0:
            self.speed -= speed_decrease
            if self.speed > 0:
                print("Your current speed is now {}km/h.".format(self.speed))
            elif self.speed == 0:
                print("Your car has stopped!")
        else:
            print("Your speed decrease is too big! Try braking a little less.")

    def fuel_up(self, amount):
        if self.start:
            print("You need to stop before filling the car.")
        elif self.start is False:
            if self.tank + amount <= self.tank_vol:
                self.tank += amount
                if self.tank == self.tank_vol:
                    print("The tank is full!")
                elif 0 < self.tank < self.tank_vol:
                    print("You have {}l in your tank now".format(self.tank))
            else:
                print("Your tank is not big enough! Try filling a little less.")

    def is_retro(self):
        if current_year - self.year > 25:
            self.retro = True
            print("You have a retro car!")
        else:
            self.retro = False
            print("Your car needs to be at least 25 years old to qualify for a retro status.")

    def __str__(self):
        return str(self.model), str(self.year)


my_car = Car("A3", 2020, 50)
my_car.is_retro()
my_car.start_up()
my_car.accelerate(50)
my_car.fuel_up(60)
my_car.fuel_up(50)
my_car.start_up()
my_car.accelerate(110)
my_car.accelerate(50)
print(my_car.tank)
my_car.brake(25)
my_car.stop()
my_car.brake(25)
my_car.stop()
print(my_car.__str__())
