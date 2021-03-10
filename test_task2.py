import unittest
import task2


class TestTask2(unittest.TestCase):

    def test_start_up(self):
        self.assertTrue(task2.my_car.start_up, True)

    def test_stop(self):
        self.assertTrue(task2.my_car.stop, False)

    def test_accelerate(self):
        self.assertEqual(task2.my_car.accelerate(50), "The car hasn't been turned on!")

    def test_brake(self):
        self.assertEqual(task2.my_car.brake(50), None)

    def test_retro(self):
        self.assertFalse(task2.my_car.retro, True)

# if __name__ == '__main__':
#     unittest.main()