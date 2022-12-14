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

    def test_combinatoria_1y4(self):
        self.assertEqual(Combinatoria.combi(1, 4), 0)

    def test_combinatoria_2y5(self):
        self.assertEqual(Combinatoria.combi(2, 5), 0)

    def test_combinatoria_3y7(self):
        self.assertEqual(Combinatoria.combi(3, 7), 0)

    def test_combinatoria_XigualN(self):
        self.assertEqual(Combinatoria.combi(3, 3), 1)

    def test_combinatoria_cadena(self):
        self.assertEqual(Combinatoria.combi("a", "b"), TypeError)

    def test_combinatoria_1y1(self):
        self.assertEqual(Combinatoria.combi(1, 1), 1)

if __name__ == "__main__":
    unittest.main()