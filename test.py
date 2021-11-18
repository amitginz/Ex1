import unittest
from  offline_algo import *


class MyTestCase(unittest.TestCase):
    def test_dist(self):
        self.assertEqual(True, False)  # add assertion here
        self.assertEqual(Offline_algo.dist(5,7,0), 4.222222222222222)
        self.assertEqual(Offline_algo.dist(-1,7,0), 12.666666666666666)
        self.assertNotEqual(Offline_algo.dist(5,7,0),0)
        self.assertNotEqual(Offline_algo.dist(-1,7,0),0)

    def test_init_from_json(self):
        reader = Offline_algo.init_from_json('B4.json')
        self.assertEqual(Offline_algo.init_from_json('B4.json'),reader)
        reader1 = Offline_algo.init_from_json('B5.json')
        self.assertEqual(Offline_algo.init_from_json('B5.json'),reader1)
        reader2 = Offline_algo.init_from_json('B1.json')
        self.assertEqual(Offline_algo.init_from_json('B1.json'),reader2)

    def test_init_from_file(self):
        reader = Offline_algo.init_from_json('Calls_a')
        self.assertEqual(Offline_algo.init_from_file('Calls_a'),reader)
        reader1 = Offline_algo.init_from_json('Calls_b')
        self.assertEqual(Offline_algo.init_from_file('Calls_b'),reader1)
        reader2 = Offline_algo.init_from_json('Calls_d')
        self.assertEqual(Offline_algo.init_from_file('Calls_d'),reader2)

    def test_allocate(self):
        a = Offline_algo.allocte('Calls_a')
        self.assertEqual(Offline_algo.init_from_file('Calls_a'),a)
        a1 = Offline_algo.allocte('Calls_b')
        self.assertEqual(Offline_algo.init_from_file('Calls_b'),a1)
        a2= Offline_algo.allocte('Calls_c')
        self.assertEqual(Offline_algo.init_from_file('Calls_c'),a2)
        self.assertNotEqual(Offline_algo.init_from_file('Calls_a'),a1)
        self.assertNotEqual(Offline_algo.init_from_file('Calls_a'),a)


if __name__ == '__main__':
    unittest.main()
