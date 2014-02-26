from general_search import GeneralSearch
from ImageTool import *


class SearchDuplicatesByRMS(GeneralSearch):
	
	def comparison_criteria(self, first_image, second_image):
		""" Compare if the size in KB is the same for two images given
			
		Keyword arguments:
		first_image -- An ImageFile object that will be compared with secon_image
		second_image -- An ImageFile object that will be compared with first_image
		
		Returned values:
		is_image_size_the_same -- It will Return True if the size of both images is the same
								It will Return False if the size of both images is not the same
		"""
		
		images_are_the_same = False
		
		input_file = first_image.get_full_path_with_name_image_type()
		input_file2 = second_image.get_full_path_with_name_image_type()
                

		image_to_compare_1 = ImageCalculator(input_file)
		image_to_compare_2 = ImageCalculator(input_file2)

		#print histogram_compare(it1, it2)
		rms_value = rmsdiff_2011(image_to_compare_1, image_to_compare_2)
				
		if (rms_value == 0):
			images_are_the_same = True
		
		return images_are_the_same	