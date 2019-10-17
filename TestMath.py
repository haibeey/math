#!/bin/bash

import unittest
from math import result,globMultipleOperation

tokensandresult={
            "1+22+33":"56",
            "1+2+(4+4)":"11",
            "(1+2+33)":"36",
            "13*(2+5*(2-3))":"-39",
            "1*(5^6)":"15625"
}

class TestMath(unittest.TestCase):
    
    def testGlobMultiple(self):
        testCases=[
                [['3', '*', '2', '+', '5', '*', '-', '1.0'],7],
                [['2', '-', '3'],3],
                [['1','+', '22', '+', '3'],5]
            ]
        for case in testCases:
            self.assertEquals(len(globMultipleOperation(case[0])),case[1])

    def test_result(self):
        for k in tokensandresult:
            token=result(k)
            self.assertEqual(token,tokensandresult[k])

if __name__ == '__main__': 
    unittest.main()
  