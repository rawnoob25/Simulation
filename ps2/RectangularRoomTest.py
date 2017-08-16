# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:26:06 2017

"""
import unittest
from ps2 import RectangularRoom, Position

class RectangularRoomTest(unittest.TestCase):
    def setUp(self):
        self.threeByFive = RectangularRoom(5,3)
        
    def testInitAndStr(self):
        print("in testInitAndStr")
        another3ByFive = [[False for i in range(5)] for j in range(3)]
        print(self.threeByFive)
        self.assertEqual(self.threeByFive.__str__(), str(another3ByFive))
    
    def testCleanTileAtPsn(self):
        print("in testCleanTileAtPsn")
        self.threeByFive.cleanTileAtPosition(Position(4.5,2.3))
        print(self.threeByFive)
        self.assertEqual(1, self.threeByFive.getNumCleanedTiles())
        self.assertTrue(self.threeByFive.isTileCleaned(4,2))
        
if __name__ == '__main__':
    unittest.main()