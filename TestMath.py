#!/bin/bash

import unittest
from math import result

tokensandresult={
            "1+22+33":"56",
            "1+2+(4+4)":"11",
            "(1+2+33)":"36",
            "13*(2+5*(2-3))":"-39",
            "1*(5^6)":"15625"
}

class TestMath(unittest.TestCase):
    
   
    def test_result(self):
        for k in tokensandresult:
            token=result(k)
            self.assertEqual(token,tokensandresult[k])

if __name__ == '__main__': 
    unittest.main()
  