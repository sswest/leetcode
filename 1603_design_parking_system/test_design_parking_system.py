from unittest import TestCase
from design_parking_system import ParkingSystem


class TestParkingSystem(TestCase):
    def test_add_car(self):
        obj = ParkingSystem(1, 1, 0)
        inputs = (('addCar', 1), ('addCar', 2), ('addCar', 3), ('addCar', 1))
        outs = (True, True, False, False)
        for inp, out in zip(inputs, outs):
            self.assertEqual(out, getattr(obj, inp[0])(inp[1]))
