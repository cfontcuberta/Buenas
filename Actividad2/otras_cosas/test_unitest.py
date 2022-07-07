import unittest
import matematicas

class Pruebasunitarias(unittest.TestCase):
    def test_factorial(selft):
        selft.assertEqual(matematicas.factorial(5), 120)
        selft.assertEqual(matematicas.hipo(2,3), 13)
        selft.assertEqual(matematicas.cuadrada(9), 3)
        selft.assertEqual(matematicas.area(3), 28.274328)
        selft.assertEqual(matematicas.rectangulo(4,5), 20)



if __name__ == '__main__':
    unittest.main()
