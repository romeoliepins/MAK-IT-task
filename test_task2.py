import unittest
import task2


# Kāpēc testiem ir nepieciešama sava jauna klase?
class TestStartUp(unittest.TestCase):

    def test_start_up_without_fuel(self):
        car = task2.Car("A3", 2020, 50)
        testing = car.start_up()
        self.assertFalse(testing)

    def test_start_up_with_fuel(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        testing = car.start_up()
        self.assertTrue(testing)

    def test_stop_without_speed(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        testing = car.stop()
        self.assertFalse(testing)

    def test_stop_with_speed(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        car.accelerate(20)
        testing = car.stop()
        self.assertTrue(testing)

    def test_accelerating_past_100(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        testing = car.accelerate(110)
        self.assertFalse(testing)

    def test_speed(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        car.accelerate(50)
        testing = car.speed
        self.assertEqual(testing, 50)

    def test_braking_less_than_speed(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        car.accelerate(50)
        car.brake(30)
        testing = car.speed
        self.assertEqual(testing, 20)

    def test_braking_more_than_speed(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        car.accelerate(50)
        testing = car.brake(60)
        self.assertFalse(testing)

    def test_braking_at_0_speed(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        testing = car.brake(20)
        self.assertFalse(testing)

    def test_braking_while_stopped(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(50)
        car.start_up()
        car.stop()
        testing = car.brake(20)
        self.assertFalse(testing)

    def test_filling_up_more_than_tank_volume(self):
        car = task2.Car("A3", 2020, 50)
        testing = car.fuel_up(60)
        self.assertFalse(testing)

    def test_fuel_after_filling_up(self):
        car = task2.Car("A3", 2020, 50)
        car.fuel_up(45)
        testing = car.tank
        self.assertEqual(testing, 45)

    def test_retro(self):
        car = task2.Car("A3", 2020, 50)
        testing = car.is_retro()
        self.assertFalse(testing)

    def test_string_implementation_of_model_and_year(self):
        car = task2.Car("A3", 2020, 50)
        testing = car.__str__()
        self.assertEqual(testing, ("A3", "2020"))


# Šo ieliku, jo pamācībā par unittestiem, tas atvieglo unittestu palaišanu terminālī.
if __name__ == '__main__':
    unittest.main()
