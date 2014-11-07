"""Unit test for Task1.py"""

import Task1
import unittest

class Requirements(unittest.TestCase):
    nameToNumberReqs = ( ("A", 0),
                         ("Z", 25),
                         ("AA", 26),
                         ("ZZZZ", 475253) )
    numberToColumnReqs = ( (0, "A"),
                           (25, "Z"),
                           (26, "AA"),
                           (475253, "ZZZZ") )

    tester = Task1.ColumnNameConversionUtility()
    
    def testNameToNumber(self):
        """columnNameToColumnNumber should give expected results"""
        for columnName, number in self.nameToNumberReqs:
            result = self.tester.columnNameToColumnNumber(columnName)
            self.assertEqual(number, result)

    def testNumberToColumnReqs(self):
        """columnNumberToColumnName should give expected results which are the inverse of columnNameToColumnNumber"""
        for columnNumber, name in self.numberToColumnReqs:
            result = self.tester.columnNumberToColumnName(columnNumber)
            self.assertEqual(name, result)

    
class NameToNumberBadInput(unittest.TestCase):
    def testLowerCase(self):
        """column names should be upper case"""
        self.assertRaises(Task1.InvalidColumnName, Task1.ColumnNameConversionUtility().columnNameToColumnNumber, "a")

    def testTooManyCharacters(self):
        """only strings in the range "A" to "ZZZZ" are accepted"""
        self.assertRaises(Task1.InvalidColumnName, Task1.ColumnNameConversionUtility().columnNameToColumnNumber, "AAAAA")

    def testNonStringColumnName(self):
        """only strings are accepted"""
        self.assertRaises(Task1.InvalidColumnName, Task1.ColumnNameConversionUtility().columnNameToColumnNumber, 5)

class NumberToNameBadInput(unittest.TestCase):
    def testInputBounds(self):
        """only integer numbers in the range 0 ... 475253 are accepted"""
        self.assertRaises(Task1.InvalidColumnNumber, Task1.ColumnNameConversionUtility().columnNumberToColumnName, -1)
        self.assertRaises(Task1.InvalidColumnNumber, Task1.ColumnNameConversionUtility().columnNumberToColumnName, 475254)

class SanityCheck(unittest.TestCase):
    def testSanity(self):
        """columnNameToColumnNumber(columnNumberToColumnName(n)) == n for all n between 0 and 475253, or A and ZZZZ"""
        for integer in range(0, 475254):
            name = Task1.ColumnNameConversionUtility().columnNumberToColumnName(integer)
            result = Task1.ColumnNameConversionUtility().columnNameToColumnNumber(name)
            self.assertEqual(integer, result)

class CaseCheck(unittest.TestCase):
    def testToColumnNameCase(self):
        """column names should be upper case"""
        for integer in range(0, 475254):
            name = Task1.ColumnNameConversionUtility().columnNumberToColumnName(integer)
            Task1.ColumnNameConversionUtility().columnNameToColumnNumber(name.upper())
            self.assertRaises(Task1.InvalidColumnName, Task1.ColumnNameConversionUtility().columnNameToColumnNumber, name.lower())

    def testToColumnNumberCase(self):
        """output must be upper case strings"""
        for integer in range(0, 475254):
            name = Task1.ColumnNameConversionUtility().columnNumberToColumnName(integer)
            self.assertEquals(name, name.upper())

if __name__ == "__main__":
    unittest.main()
                          
