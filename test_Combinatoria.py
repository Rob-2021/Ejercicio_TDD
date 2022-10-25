from msilib.schema import Error
import unittest
import Combinatoria

class TestMyCombinatoria(unittest.TestCase):
    def test_combinatoria5y2(self):
        self.assertEqual(Combinatoria.combi(5, 2), 360)

if __name__ == "__main__":
    unittest.main()