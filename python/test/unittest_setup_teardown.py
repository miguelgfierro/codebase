import unittest
import xmlrunner
import pandas as pd
import numpy as np


class DummyUnitTest(unittest.TestCase):
    def setUp(self):
        self.int = 1
        self.yes = True
        self.no = False
        self.float = 0.5
        self.pi = 3.141592653589793238462643383279
        self.string = "Miguel"
        self.list = [1, 2, 3]
        self.dict = {'a': 1, 'b': 2, 'c': 3}
        self.none = None
        self.np_array = np.array(self.list)
        self.df = pd.DataFrame(self.list)

    def tearDown(self):
        pass

    def test_basic_structures(self):
        self.assertEqual(self.int, 1)
        self.assertTrue(self.yes)
        self.assertFalse(self.no)
        self.assertEqual(self.float, 0.5)
        self.assertAlmostEqual(self.pi, 3.1415926, places=6)
        self.assertNotAlmostEqual(self.pi, 3.1415926, places=7)
        self.assertEqual(self.string, "Miguel")


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
