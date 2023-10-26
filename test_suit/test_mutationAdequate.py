import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify( -10 , 10 , 10 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify( 9 , 10, 11 )
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)


    def test4(self):
        actual = Triangle.classify( 9 , 9, 11 )
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify( 9 , 11, 9 )
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify( 11 , 9 , 9 )
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify( 4 , 5 , 14 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify( 14 , 4 , 4 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test9(self):
        actual = Triangle.classify( 0,2,2 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test10(self):
        actual = Triangle.classify( 2,0,2 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test11(self):
        actual = Triangle.classify( 2,2,0 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test12(self):
        actual = Triangle.classify( 2,2,4 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test13(self):
        actual = Triangle.classify( 2,4,2 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test14(self):
        actual = Triangle.classify( 4,2,2 )
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    

if __name__ == '__main__':
    unittest.main()