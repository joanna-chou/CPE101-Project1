# Project 1 Fitness Tracking Tests
# At least 2 tests for each function
# Name: Joanna Chou
# Section: 07
# Date: 1/15/2022

import unittest
from fitnessTrackerFuncs import *
class MyTestCase(unittest.TestCase):
    def test_convert_lb_to_kg(self):
        self.assertAlmostEqual(convert_lb_to_kg(110), 49.895160700000005)
        self.assertAlmostEqual(convert_lb_to_kg(188), 85.27536556)
    
    def test_compute_MET(self):
        self.assertAlmostEqual(compute_MET(1), 5)
        self.assertAlmostEqual(compute_MET(4), 4)

    def test_compute_calorie_burned(self):
        self.assertAlmostEqual(compute_calorie_burned(50,78,5), 341.25)
        self.assertAlmostEqual(compute_calorie_burned(77,90,7), 848.9250000000001)

    def test_compute_BMI(self):
        self.assertAlmostEqual(compute_BMI(110,68), 16.723615916955016)
        self.assertAlmostEqual(compute_BMI(170,67), 26.62285586990421)
    
    def test_BMI_category(self):
        self.assertAlmostEqual(BMI_category(16.7), "Underweight")
        self.assertAlmostEqual(BMI_category(26.6), "Over Weight")

    def test_compute_equivalent_miles(self):
        self.assertAlmostEqual(compute_equivalent_miles(68,1,65),3.457310606060606)
        self.assertAlmostEqual(compute_equivalent_miles(50,4,45),2.229261363636364)

if __name__ == '__main__':
    unittest.main()