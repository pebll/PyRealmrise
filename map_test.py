import unittest
from map import Map
from ressource import Ressource

class TestMapMethods(unittest.TestCase):

    def setUp(self):
        self.map = Map(5,5)  # initialize your class

    def test_harvest(self):
        self.assertEqual(self.map.map[0][0].harvest(Ressource.GRASS), 1)


if __name__ == '__main__':
    unittest.main()