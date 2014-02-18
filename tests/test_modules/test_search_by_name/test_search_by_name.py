import unittest
import sys
import os.path

sys.path.append("../../../")
from main.modules.image_modules.imageFile import ImageFile
from main.modules.searcher_module.search_by_name import SearchDuplicatesByName
from main.modules.list_images_module.list_images import ListImages


class TestSearchByName(unittest.TestCase):
	
	def setUp(self):
		self.test_path, not_needed_current_dir = os.path.split(os.getcwd())
		self.search_by_name = SearchDuplicatesByName()
		self.list_images = ListImages()
			
	def test_search_by_name_returnd_a_list_of_duplicate_images(self):
		list_of_images = []
		self.test_path = self.test_path + "/images_for_unittest"
		self.list_of_directories = self.list_images.get_all_nested_directories(self.test_path)
		size_of_list_of_folders = len(self.list_of_directories)
		list_of_images_duplicates_expected = []
		list_of_images_obtained = self.list_images.get_all_images_from_directory \
								(size_of_list_of_folders, list_of_images, self.list_of_directories)
		print list_of_images_obtained
		list_of_images_dupes_by_name = self.search_by_name.search_duplicates(list_of_images_obtained)
		self.assertEquals(list_of_images_dupes_by_name, list_of_images_duplicates_expected)
		

if __name__ == '__main__':
	unittest.main()