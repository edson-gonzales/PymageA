import unittest
import sys
import os
sys.path.append("../../../")
from main.modules.image_modules.imageFile import ImageFile

class TestImageFile(unittest.TestCase):
	image_file_test=' '
	path_resources=' '

	def setUp(self):
		unittest.TestCase.setUp(self)
		self.image_file_test=ImageFile()
		self.path_resources= os.path.dirname(os.path.abspath(__file__))+'/resources/'
				
	def test_validate_image_return_TRUE_if_file_type_JPG_exist_in_path(self):
		self.assertTrue(self.image_file_test.validate_image(self.path_resources,"balon.jpg"))

	def test_validate_image_return_TRUE_if_file_type_BMP_exist_in_path(self):
		self.assertTrue(self.image_file_test.validate_image(self.path_resources,"T-shirt.bmp"))

	def test_validate_image_return_TRUE_if_file_type_PNG_exist_in_path(self):
		self.assertTrue(self.image_file_test.validate_image(self.path_resources,"equipo.png"))

	def test_validate_image_return_FALSE_if_file_type_is_not_valid_type(self):
		self.assertFalse(self.image_file_test.validate_image(self.path_resources,"mytest.txt"))
		
	def test_validate_image_return_FALSE_if_file_is_not_exist(self):
		self.assertFalse(self.image_file_test.validate_image(self.path_resources,"nofile.png"))

	def test_validate_image_return_FALSE_if_incorrect_path(self):
		self.assertFalse(self.image_file_test.validate_image('c:/no path',"balon.jpg"))

	def test_validate_image_return_FALSE_if_incorrect_path_and_incorrect_file_image(self):
		self.assertFalse(self.image_file_test.validate_image('c:/no path',"balonjpg"))

	def test_set_image_values_return_TRUE_if_attributes_to_imageFile_are_set_with_correct_values(self):
		self.assertTrue(self.image_file_test.set_image_values(self.path_resources,"balon.jpg"))

	def test_set_image_values_return_False_if_attributes_to_imageFile_are_not_set(self):
		self.assertFalse(self.image_file_test.set_image_values(self.path_resources,"mytest.txt"))
	
		


if __name__=="__main__":
	unittest.main()

