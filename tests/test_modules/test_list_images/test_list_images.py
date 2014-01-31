import unittest
import sys
import os.path

main_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, os.path.pardir, os.path.pardir))
path_to_add = main_path + "\\main\\modules\\list_images_module" 
sys.path.append(path_to_add)


from list_images import ListImages

class TestListImages(unittest.TestCase):
	
			
	def test_list_images_of_specified_directory(self):
		pass
		list_images = ListImages()
		test_path, not_neede_current_dir = os.path.split(os.getcwd())
		test_path = test_path + "\\images_for_unittest"
		list_of_current_images_on_directory = ['Image1.jpg','Image2.png','Image3.bmp']
		list_of_images_from_get_all_images_from_home = list_images.get_all_images_from_path(test_path)
		self.assertEquals(list_of_current_images_on_directory,list_of_images_from_get_all_images_from_home )
		
if __name__ == '__main__':
	unittest.main()
