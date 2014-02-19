import unittest
import sys
import os.path
import shutil

sys.path.append("../../../")
from main.modules.list_images_module.list_images import ListImages
from main.modules.searcher_module.search_by_name import SearchDuplicatesByName
from main.modules.searcher_module.search_by_size import SearchDuplicatesBySize
from main.modules.image_modules.imageFile import ImageFile


class TestListImages(unittest.TestCase):
	
	list_images = ''
	test_path = ''
	list_of_directories = []
	
	
	def setUp(self):
		self.list_images = ListImages()
		self.test_path, not_needed_current_dir = os.path.split(os.getcwd())
		self.message = ""
	
	def are_items_equal(self, list_of_images_expected, list_of_images_obtained):
		are_equal = True
		if len(list_of_images_expected) == len(list_of_images_obtained):
			for image_object in list_of_images_obtained:
				if image_object.get_complete_image_with_type() not in list_of_images_expected:
					are_equal = False	
					self.message = "Not equal. " + image_object.get_complete_image_with_type() + " \
									not in " + ', '.join(list_of_images_expected)
		else:
			are_equal = False
			self.message("Not equal. The length of lists is different")
		return are_equal
	
	def is_item_in_list(self, item, list_of_images_obtained):
		is_item_in_list = False
		self.message = "Item is not there. "
		for image_object in list_of_images_obtained:
				if item.get_complete_image_with_type() == image_object.get_complete_image_with_type():
					is_item_in_list = True
					self.message = "Item is there."
		return is_item_in_list
			
	
	def test_list_images_in_specified_scope_of_specified_directory(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['balon.jpg','equipo.png','T-shirt.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		if self.are_items_equal(list_of_images_expected, list_of_images_obtained) == False:
			self.fail(self.message)
	
	def test_list_only_images_in_specified_scope_of_specified_directory(self):
		list_of_images = []
		self.test_path = self.test_path + "/images2_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['balon.jpg','equipo.png','T-shirt.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		if self.are_items_equal(list_of_images_expected, list_of_images_obtained) == False:
			self.fail(self.message)
		
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
		if self.are_items_equal(list_of_images_expected, list_of_images_obtained) == False:
			self.fail(self.message)
	
	def test_list_images_returns_images_and_not_directories(self):
		list_of_images = []
		self.test_path = self.test_path + "/images4_for_unit_test"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['balon.jpg','equipo.png','T-shirt.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		if self.are_items_equal(list_of_images_expected, list_of_images_obtained) == False:
			self.fail(self.message)
	
	def test_directories_from_user_are_returned_if_empty_path(self):
		list_of_images = []
		path_of_image_to_copy_to_user_home = os.path.abspath(self.test_path + "/images_for_unittest/balon.jpg")
		user_home_images_directory_path = os.path.expanduser('~') + "/" + "Images/"
		# If there is some permissions error
		try:
			shutil.copy(path_of_image_to_copy_to_user_home, user_home_images_directory_path)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
		
		self.list_of_directories = self.list_images.get_all_nested_directories("")
		size_of_list_of_folders = len(self.list_of_directories)
		
		image_expected = ImageFile()
		image_expected.verify_image_values(user_home_images_directory_path,'balon.jpg')
		list_of_images_obtained = self.list_images.get_all_images_from_directory\
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		if self.is_item_in_list(image_expected, list_of_images_obtained) == False:
			self.fail(self.message)
	
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
		if self.are_items_equal(duplicated_images, list_of_images_to_look_for) == False:
			self.fail(self.message)
	
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
		if self.are_items_equal(duplicated_images, list_of_images_to_look_for) == False:
			self.fail(self.message)

if __name__ == '__main__':
	unittest.main()