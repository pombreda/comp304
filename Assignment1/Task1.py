# -*- coding: utf-8 -*-
class ColumnNameConversionUtility:
    def columnNameToColumnNumber(self, columnName):
        """
            Transform strings used as cell column names (e.g., "A" in the cell reference "A5") to integers (for efficiency reasons).
            Requirements:
            - "A" is converted to 0
            - "Z" is converted to 25
            - "AA" follows "Z" and is converted to 26, and so on
            - only strings in the range "A" to "ZZZZ" are accepted
            - column names should be upper case
            - in case of an improper columnName input, the InvalidColumnName exception should be raised
        """
        if (type(columnName) != str):
            raise InvalidColumnName(str(columnName) + " is not a string")

        if(len(columnName) > 4):
            raise InvalidColumnName(columnName + " is not in the range \"A\" to \"ZZZZ\"")

        columnNumber = -1
        
        for c in columnName:
            if (ord(c) < 65 or ord(c) > 90):
                raise InvalidColumnName("Column names should be upper case")
            columnNumber += 1
            columnNumber *= 26
            columnNumber += ord(c) - 65
        
        return columnNumber

    def columnNumberToColumnName(self, columnNumber):
        """
          Requirements:
           - inverse of columnNameToColumnNumber
           - only integer numbers in the range 0 .. columnNameToColumnNumber("ZZZZ") are allowed as input
           - output must be upper case strings: in case of an improper columnNumber input, the InvalidColumnNumber exception should be raised
        """
        if (type(columnNumber) != int):
            raise InvalidColumnNumber(str(columnNumber) + " is not an integer")

        if (columnNumber < 0 or columnNumber > 475253):
            raise InvalidColumnNumber(str(columnNumber) + " is out of range.  Valid range is 0 - 475253")

        columnName = ""

        while columnNumber >= 0:
            c = columnNumber % 26
            columnName = chr(c + 65) + columnName
            columnNumber -= c
            columnNumber /= 26
            columnNumber -= 1
            
        return columnName
    
class InvalidColumnName(Exception):
    """Invalid input for a column name"""
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

class InvalidColumnNumber(Exception):
    """Invalid input for a column number"""
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
