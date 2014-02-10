import unittest
import os
from logger import mylogger

class ListloggerTest(unittest.TestCase):
	def test_file_exist(mypath):
		assert os.path.isdir(mypath)
		#assert os.path.isdir('C:\Users\mauricio\Desktop\Phyton\ejer\logger1/myapp.log')
		

if __name__== "__main__":
	unittest.main()	
	test_file_exist('C://Users//mauricio//Desktop//Phyton//ejer//logger1')	