import unittest
from mathutils.algebra import solve_linear 

class TestAlgebra(unittest.TestCase):
    def test_solve_linear(self):
        result = solve_linear(2, 4)  # Example test
        self.assertEqual(result, -2)  # 2x + 4 = 0 → x = -2

if __name__ == '__main__':
    unittest.main()
