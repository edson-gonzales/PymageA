import unittest
import sys
import os
sys.path.append("../../../")

from main.modules.image_modules.imageFile import ImageFile


class TestImageFile(unittest.TestCase):
	image_file_test = ' '
	path_resources = ' '

	def setUp(self):
		unittest.TestCase.setUp(self)
		self.image_file_test = ImageFile()
		self.path_resources = os.path.dirname(os.path.abspath(__file__)) + '/resources/'
				
	def test_is_valid_image_return_TRUE_if_file_type_JPG_exist_in_path(self):
		self.assertTrue(self.image_file_test.is_valid_image(self.path_resources, 'balon.jpg'))

	def test_is_valid_image_return_TRUE_if_file_type_BMP_exist_in_path(self):
		self.assertTrue(self.image_file_test.is_valid_image(self.path_resources, 'T-shirt.bmp'))

	def test_is_valid_image_return_TRUE_if_file_type_PNG_exist_in_path(self):
		self.assertTrue(self.image_file_test.is_valid_image(self.path_resources, 'equipo.png'))

	def test_is_valid_image_return_FALSE_if_file_type_is_not_valid_type(self):
		self.assertFalse(self.image_file_test.is_valid_image(self.path_resources, 'mytest.txt'))
		
	def test_is_valid_image_return_FALSE_if_file_is_not_exist(self):
		self.assertFalse(self.image_file_test.is_valid_image(self.path_resources, 'nofile.png'))

	def test_is_valid_image_return_FALSE_if_incorrect_path(self):
		self.assertFalse(self.image_file_test.is_valid_image('c:/no path', 'balon.jpg'))

	def test_is_valid_image_return_FALSE_if_incorrect_path_and_incorrect_file_image(self):
		self.assertFalse(self.image_file_test.is_valid_image('c:/no path', 'balonjpg'))

	def test_verify_image_values_return_TRUE_if_attributes_to_imageFile_are_set_with_correct_values(self):
		self.assertTrue(self.image_file_test.verify_image_values(self.path_resources, 'balon.jpg'))


	def test_verify_image_values_return_FALSE_if_attributes_to_imageFile_are_not_set(self):
		self.assertFalse(self.image_file_test.verify_image_values(self.path_resources, 'mytest.txt'))
	
	def test_is_valid_size_image_return_TRUE_if_with_500_and_hihg_100_are_in_range(self):
		self.assertTrue(self.image_file_test.is_valid_size_image(500, 100))

	def test_is_valid_size_image_return_FALSE_if_withsize_100_negative_and_hihgsize_100_are_not_in_range(self):
		self.assertFalse(self.image_file_test.is_valid_size_image(-100, 100))
	
	def test_is_valid_size_image_return_FALSE_if_any_size_is_a_decimal_number(self):
		self.assertFalse(self.image_file_test.is_valid_size_image(12.3, 100))

	def test_resize_image_return_TRUE_if_image_is_resized_with_new_sizes_interger_values(self):
		resul = self.image_file_test.verify_image_values(self.path_resources, 'T-shirt.bmp')
		self.assertTrue(self.image_file_test.resize_image(10, 10))

	def test_resize_image_return_FALSE_if_image_is_not_resized_with_new_sizes_decimal_values(self):
		resul = self.image_file_test.verify_image_values(self.path_resources, 'T-shirt.bmp')	
		self.assertFalse(self.image_file_test.resize_image(10.4, 400))

	def test_resize_image_return_FALSE_if_image_is_not_resized_with_new_sizes_negative_integer_values(self):
		resul = self.image_file_test.verify_image_values(self.path_resources, 'T-shirt.bmp')	
		self.assertFalse(self.image_file_test.resize_image(-10, 400))

	def test_is_valid_angle_image_return_TRUE_if_integer_angle_is_valid(self):
		self.assertTrue(self.image_file_test.is_valid_angle_image(10))

	def test_is_valid_angle_image_return_FALSE_if_angle_with_decimal_value_is_not_valid(self):
		self.assertFalse(self.image_file_test.is_valid_angle_image(10.3))

	def test_rotate_image_return_TRUE_if_image_with_integer_angle_is_rotated(self):
		resul = self.image_file_test.verify_image_values(self.path_resources, 'equipo.png')	
		self.assertTrue(self.image_file_test.rotate_image(-50))

	def test_rotate_image_return_FALSE_if_image_is_not_rotate_with_integer_angle_out_of_range(self):
		resul = self.image_file_test.verify_image_values(self.path_resources, 'balon.png')	
		self.assertFalse(self.image_file_test.rotate_image(182))