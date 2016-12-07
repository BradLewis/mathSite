from django.test import TestCase

from .views import getNumber

#Test cases to test the various inputs
class testMethods(TestCase):
    def testZero(self):
        output = getNumber(0)
        expectedOutput = "You cannot have a 0 sided dice! Please enter a valid number"
        self.assertTrue(output == expectedOutput)

    def testNegative(self):
        output = getNumber(-0.8)
        expectedOutput = "Whoops! That is not a valid number, please enter a valid number (remember a dice can only have an integer number of sides)"
        self.assertTrue(output == expectedOutput)

    def testRandom(self):
        output = getNumber("0afndslslkdf\"$@^%&56")
        expectedOutput = "Whoops! That is not a valid number, please enter a valid number (remember a dice can only have an integer number of sides)"
        self.assertTrue(output == expectedOutput)

    def testlarge(self):
        output = getNumber("999")
        expectedOutput = "The probability of rolling a 890 sided dice 890 times and each side comes up only once is approximately 0"
        self.assertTrue(output == expectedOutput)

    def testNegativeLarge(self):
        output = getNumber(-1008)
        expectedOutput = "Whoops! That is not a valid number, please enter a valid number (remember a dice can only have an integer number of sides)"
        self.assertTrue(output == expectedOutput)
