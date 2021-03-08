import unittest
import sys
import fizzBuzz
#solution to check stdout found from https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python/17981937
class TestCase(unittest.TestCase):
	def test_prints(self):
		#calls print function of program
		fizzBuzz.prints()
		#check if using buffer
		if not hasattr(sys.stdout,"getvalue"):
			self.fail("need to run in buffered mode")
		#save stdout as ouput
		output = sys.stdout.getvalue().strip()
		#compares stdout with that it's supposed to be
		self.assertEquals(output,'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz')
if __name__ == '__main__':
	assert not hasattr(sys.stdout,"getvalue")
	unittest.main(module=__name__, buffer = True,exit=False)





