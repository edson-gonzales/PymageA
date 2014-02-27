import unittest
import sys
import os.path

sys.path.append("../../../")
from src.modules.image_modules.imageFile import ImageFile
from src.modules.searcher_module.search_by_name import SearchDuplicatesByName
from src.modules.list_images_module.list_images import ListImages
from tests.test_modules.comparison_tools import *

class TestSearchByName(unittest.TestCase):
	
	def setUp(self):
		self.test_path = os.getcwd() 
                self.search_by_name = SearchDuplicatesByName()
		self.list_images = ListImages()
		self.message = ""

	def test_search_by_name_returnd_a_list_of_duplicate_images_when_one_duplicated(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_test_duplicates"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_duplicates_expected = ['balon.jpg','balon.jpg']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		list_of_images_dupes_by_name = self.search_by_name.search_duplicates(list_of_images_obtained)
		res = are_items_equal(list_of_images_duplicates_expected, list_of_images_dupes_by_name)
		self.assertTrue(res[0], res[1])
	
	def test_search_by_name_returnd_a_list_of_duplicate_images_when_two_duplicated(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_test_duplicates2"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_duplicates_expected = ['balon.jpg','balon.jpg','balon.jpg']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		list_of_images_dupes_by_name = self.search_by_name.search_duplicates(list_of_images_obtained)
		res = are_items_equal(list_of_images_duplicates_expected, list_of_images_dupes_by_name)
		self.assertTrue(res[0], res[1])
	
	def test_search_by_name_returnd_a_list_of_duplicate_images_when_two_different_images_are_duplicated(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_test_duplicates3"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_duplicates_expected = ['balon.jpg','balon.jpg','balon.jpg','equipo.png','equipo.png']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		list_of_images_dupes_by_name = self.search_by_name.search_duplicates(list_of_images_obtained)
		res = are_items_equal(list_of_images_duplicates_expected, list_of_images_dupes_by_name)
		self.assertTrue(res[0], res[1])
	
	def test_show_images(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_test_duplicates3"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_duplicates_expected = ['balon.jpg','balon.jpg','balon.jpg','equipo.png','equipo.png']
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		
		list_of_images_dupes_by_name = self.search_by_name.search_duplicates(list_of_images_obtained)
		self.search_by_name.show_path_of_duplicated_images()

if __name__ == "__main__":
    unittest.main()