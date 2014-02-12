import unittest
import sys
import os.path
import shutil

sys.path.append("../../../")
from main.modules.list_images_module.list_images import ListImages
from main.modules.searcher_module.search_by_name import SearchDuplicatesByName


class TestListImages(unittest.TestCase):
	
	list_images = ''
	test_path = ''
	list_of_directories = []
	
	
	def setUp(self):
		self.list_images = ListImages()
		self.test_path, not_needed_current_dir = os.path.split(os.getcwd())
			
	def test_list_images_in_specified_scope_of_specified_directory(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['Image1.jpg','Image2.png','Image3.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		self.assertEquals(list_of_images_expected, list_of_images_obtained)
		
	def test_list_only_images_in_specified_scope_of_specified_directory(self):
		list_of_images = []
		self.test_path = self.test_path + "/images2_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['Image1.jpg','Image2.png','Image3.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		self.assertItemsEqual(list_of_images_expected, list_of_images_obtained)	
	
	def test_is_file_in_image_scope_return_true_for_jpg(self):
		return self.assertTrue(self.list_images.is_file_in_image_scope('.jpg'))
		
	def test_list_images_in_specified_scope_of_specified_directory_and_nested_directories(self):
		list_of_images = []
		self.test_path = self.test_path + "/images3_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['Image4.jpg','Image1.jpg','Image2.png',\
								   'Image3.bmp','Image1.jpg','Image2.png',\
								   'Image3.bmp','Image1.jpg','Image2.png',\
								   'Image3.bmp'\
									]
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		self.assertItemsEqual(list_of_images_expected, list_of_images_obtained)	
	
	def test_list_images_returns_images_and_not_directories(self):
		list_of_images = []
		self.test_path = self.test_path + "/images4_for_unit_test"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_expected = ['Image1.jpg','Image2.png','Image3.bmp']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		self.assertItemsEqual(list_of_images_expected, list_of_images_obtained)
	
	def test_directories_from_user_are_returned_if_empty_path(self):
		list_of_images = []
		path_of_image_to_copy_to_user_home = os.path.abspath(self.test_path + "/images_for_unittest/Image1.jpg")
		user_home_images_directory_path = os.path.abspath(os.path.expanduser('~') + "/" + "Pictures")
		# If there is some permissions error
		try:
			shutil.copy(path_of_image_to_copy_to_user_home, user_home_images_directory_path)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
		
		self.list_of_directories = self.list_images.get_all_nested_directories("")
		size_of_list_of_folders = len(self.list_of_directories)
		
		image_expected = 'Image1.jpg'
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		self.assertTrue(image_expected in list_of_images_obtained)
	
	def test_search_returns_a_concrete_search_on_given_path(self):
		list_of_images = []
		self.test_path = self.test_path + "/images4_for_unit_test"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		search_type = SearchDuplicatesByName()
		duplicated_images = ['Image1.jpg','Image2.png','Image3.bmp']
		list_of_images_to_look_for = self.list_images.search_images_in_path \
									(self.test_path, search_type, size_of_list_of_folders, list_of_images, self.list_of_directories) 
		
		self.assertItemsEqual(duplicated_images, list_of_images_to_look_for)

if __name__ == '__main__':
	unittest.main()