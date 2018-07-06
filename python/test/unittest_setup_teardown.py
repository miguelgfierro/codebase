import unittest
import xmlrunner
import pandas as pd
import numpy as np


class DummyUnitTest(unittest.TestCase):
    def setUp(self):
        self.int = 5
        self.yes = True
        self.no = False
        self.float = 0.5
        self.pi = 3.141592653589793238462643383279
        self.string = "Miguel"
        self.none = None
        self.list = [1, 2, 3]
        self.dict = {'a': 1, 'b': 2}
        self.np_array = np.array(self.list)
        self.df = pd.DataFrame(self.dict, index=[0])

    def tearDown(self):
        pass

    def test_basic_structures(self):
        self.assertEqual(self.int, 5)
        self.assertTrue(self.yes)
        self.assertFalse(self.no)
        self.assertEqual(self.float, 0.5)
        self.assertEqual(self.string, "Miguel")
        self.assertIsNone(self.none)
        self.assertIsNotNone(self.int)

    def test_comparing_numbers(self):
        self.assertAlmostEqual(self.pi, 3.1415926, places=6)
        self.assertNotAlmostEqual(self.pi, 3.1415926, places=7)
        self.assertGreater(self.int, 3)
        self.assertGreaterEqual(self.int, 5)
        self.assertLess(self.int, 10)
        self.assertLessEqual(self.int, 5)

    def test_lists(self):
        self.assertListEqual(self.list, [1, 2, 3])
        self.assertCountEqual(self.list, [2, 1, 3])
        self.assertIn(1, self.list)
        sublist_in_list = all(x in self.list for x in [1, 2])
        self.assertTrue(sublist_in_list)
        self.assertNotIn(5, self.list)

    def test_dictionaries(self):
        self.assertDictEqual(self.dict, {'a': 1, 'b': 2})
        self.assertDictContainsSubset(self.dict, {'a': 1, 'b': 2, 'c': 3}) # deprecated (no alternative)
        self.assertRaises(KeyError, lambda: self.dict['c'])
        self.assertIn('a', self.dict)

    def test_pandas(self):
        df_target = pd.DataFrame({'a': 1, 'b': 2}, index=[0])
        self.assertTrue((self.df.equals(df_target)))
        pd.testing.assert_frame_equal(self.df, df_target)  # same as before

    def test_numpy(self):
        np_target = np.array([1, 2, 3])
        np_target2 = np.array([0.9999, 2, 3])
        self.assertTrue((self.np_array == np_target).all())
        np.testing.assert_array_equal(self.np_array, np_target)
        np.testing.assert_array_almost_equal(
            self.np_array, np_target2, decimal=4)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
