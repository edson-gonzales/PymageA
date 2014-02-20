import unittest
import sys
import os.path
import shutil

sys.path.append("../../")
from main.modules.list_images_module.list_images import ListImages
from main.modules.searcher_module.search_by_name import SearchDuplicatesByName
from main.modules.searcher_module.search_by_size import SearchDuplicatesBySize
from main.modules.image_modules.imageFile import ImageFile
from tests.test_modules.comparison_tools import *

class TestListImages(unittest.TestCase):
	
	list_images = ''
	test_path = ''
	list_of_directories = []
	
	
	def setUp(self):
		self.list_images = ListImages()
		self.test_path = os.getcwd()
		self.message = ""
	
	def test_list_images_in_specified_scope_of_specified_directory(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['balon.jpg','equipo.png','T-shirt.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		result_and_message = are_items_equal(list_of_images_expected, list_of_images_obtained)
		self.assertTrue(result_and_message[0], result_and_message[1])
			
	
	def test_list_only_images_in_specified_scope_of_specified_directory(self):
		list_of_images = []
		self.test_path = self.test_path + "/images2_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['balon.jpg','equipo.png','T-shirt.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		result_and_message = are_items_equal(list_of_images_expected, list_of_images_obtained)
		self.assertTrue(result_and_message[0], result_and_message[1])	
			
		
	def test_is_file_in_image_scope_return_true_for_jpg(self):
		return self.assertTrue(self.list_images.is_file_in_image_scope('.jpg'))
		
	def test_list_images_in_specified_scope_of_specified_directory_and_nested_directories(self):
		list_of_images = []
		self.test_path = self.test_path + "/images3_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['balon.jpg','equipo.png','T-shirt.bmp',\
								   'balon.jpg','equipo.png','T-shirt.bmp',\
								   'balon.jpg','equipo.png','T-shirt.bmp',\
								   'balon.jpg'\
									]
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		result_and_message = are_items_equal(list_of_images_expected, list_of_images_obtained)
		self.assertTrue(result_and_message[0],result_and_message[1])
	
	def test_list_images_returns_images_and_not_directories(self):
		list_of_images = []
		self.test_path = self.test_path + "/images4_for_unit_test"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['balon.jpg','equipo.png','T-shirt.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		if are_items_equal(list_of_images_expected, list_of_images_obtained) == False:
			self.fail(self.message)
	
	def test_directories_from_user_are_returned_if_empty_path(self):
		list_of_images = []
		path_of_image_to_copy_to_user_home = os.path.abspath(self.test_path + "/images_for_unittest/balon.jpg")
		user_home_images_directory_path = os.path.expanduser('~') + "/" + "Images/"
		# If there is some permissions error
		try:
			shutil.copy(path_of_image_to_copy_to_user_home, user_home_images_directory_path)
		except Exception as e:
			print e
		
		self.list_of_directories = self.list_images.get_all_nested_directories("")
		size_of_list_of_folders = len(self.list_of_directories)
		
		image_expected = ImageFile()
		image_expected.verify_image_values(user_home_images_directory_path,'balon.jpg')
		list_of_images_obtained = self.list_images.get_all_images_from_directory\
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		result_and_message =  is_item_in_list(image_expected, list_of_images_obtained)
		self.assertTrue(result_and_message[0], result_and_message[1])
	
	def test_search_returns_a_earch_by_name_on_given_path(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_test_duplicates2"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		search_type = SearchDuplicatesByName()
		duplicated_images = ['balon.jpg','balon.jpg','balon.jpg']
		list_of_images_to_look_for = self.list_images.search_images_in_path \
									(self.test_path, search_type, size_of_list_of_folders, \
									list_of_images, self.list_of_directories) 
		result_and_message = are_items_equal(duplicated_images, list_of_images_to_look_for)
		self.assertTrue(result_and_message[0], result_and_message[1])
	
	def test_search_returns_search_by_size_on_given_path(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_test_duplicates2"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		search_type = SearchDuplicatesBySize()
		duplicated_images = ['balon.jpg','balon.jpg','balon.jpg']
		list_of_images_to_look_for = self.list_images.search_images_in_path \
									(self.test_path, search_type, size_of_list_of_folders, \
									list_of_images, self.list_of_directories) 
		result_and_message = are_items_equal(duplicated_images, list_of_images_to_look_for)
		self.assertTrue(result_and_message[0], result_and_message[1])

