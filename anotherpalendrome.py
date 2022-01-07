from icecream import ic
import unittest


#orgword = input("what word should we check? ")

def findPalendrome(word):
    ic(len(word))
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and findPalendrome(word[1:-1])

print(findPalendrome("orgword"))

class SimpleTest(unittest.TestCase):
    
    def test(self):
        self.assertTrue(findPalendrome("abba"))

    def testFalse(self):
        self.assertFalse(findPalendrome("abcdefedcb"))