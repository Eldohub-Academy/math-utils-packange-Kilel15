import unittest
from mathutils.geometry import area_circle, perimeter_circle, area_rectangle, perimeter_rectangle

class TestGeometry(unittest.TestCase):
    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(1), 3.141592653589793)
        self.assertAlmostEqual(area_circle(2), 12.566370614359172)
        self.assertAlmostEqual(area_circle(0), 0)
        with self.assertRaises(ValueError):
            area_circle(-1)

    def test_perimeter_circle(self):
        self.assertAlmostEqual(perimeter_circle(1), 6.283185307179586)
        self.assertAlmostEqual(perimeter_circle(2), 12.566370614359172)
        self.assertAlmostEqual(perimeter_circle(0), 0)
        with self.assertRaises(ValueError):
            perimeter_circle(-1)

    def test_area_rectangle(self):
        self.assertEqual(area_rectangle(2, 3), 6)
        self.assertEqual(area_rectangle(5, 4), 20)
        self.assertEqual(area_rectangle(0, 5), 0)
        with self.assertRaises(ValueError):
            area_rectangle(-2, 3)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter_rectangle(2, 3), 10)
        self.assertEqual(perimeter_rectangle(5, 4), 18)
        self.assertEqual(perimeter_rectangle(0, 5), 10)
        with self.assertRaises(ValueError):
            perimeter_rectangle(-2, 3)

if __name__ == '__main__':
    unittest.main()
