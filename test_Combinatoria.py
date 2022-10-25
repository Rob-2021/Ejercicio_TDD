from msilib.schema import Error
import unittest
import Combinatoria

class TestMyCombinatoria(unittest.TestCase):
    def test_combinatoria5y2(self):
        self.assertEqual(Combinatoria.combi(5, 2), 360)

    def test_combinatoriaXnegativo(self):
        self.assertEqual(Combinatoria.combi(-5, 2), 0)

    def test_combinatoriaNnegativo(self):
        self.assertEqual(Combinatoria.combi(5, -2), 0)

    def test_combinatoria_0y3(self):
        self.assertEqual(Combinatoria.combi(0, 3), 0)

if __name__ == "__main__":
    unittest.main()