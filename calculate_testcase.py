import unittest


class Testcalculate_addition(unittest.TestCase):
    def test_001_calculate_addition(self):
        a = 10
        b = 20
        c = calculate_addition(a, b)
        self.assertEqual(c, 30)
    
    def test_001_calculate_subtraction(self, a, b):
        a = 20
        b = 10
        c = calculate_subtraction(a,b)
        self.assertEqual(c, 10)
    
    def test_001_calculate_addition(self, a, b):
        a = 5.0
        b = 4.9
        c = calculate_addition(a,b)
        self.assertEqual(c, 9.9)

    def test_001_calculate_addition(self, a, b):
        a = "ab"
        b = "cd"
        c = calculate_addition(a,b)
        self.assertEqual(c, "abcd")
        with self.assertRaises(TypeError):
            c.calculate_addition(2)
  
        
if __name__ == '__main__':
    unittest.main()
