import unittest
from math import tokenize,processString

tokensandresult={
            "1+22+33":["1","+","22","+","33"],
            "1+2+(4+4)":["1","+","2","+","(4+4)"],
            "(1+2+33)":["(1+2+33)"],
            "13*(2+5*(2-3))":["13","*","(2+5*(2-3))"]
}

class TestMath(unittest.TestCase):
    def test_tokenize(self):
        
        for k in tokensandresult:
            token=tokenize(k)
            print(token,tokensandresult[k])
            self.assertEqual(token, tokensandresult[k]) 
    def test_result(self):
        
        for k in tokensandresult:
            token=processString(k)
            print(token)

if __name__ == '__main__': 
    unittest.main()
  