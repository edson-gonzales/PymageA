from general_search import GeneralSearch

class SearchDuplicatesBySize(GeneralSearch):
	
	def comparison_criteria(self, first_image, second_image):
		""" Compare if the size in KB is the same for two images given
			
		Keyword arguments:
		first_image -- An ImageFile object that will be compared with secon_image
		second_image -- An ImageFile object that will be compared with first_image
		
		Returned values:
		is_image_size_the_same -- It will Return True if the size of both images is the same
								It will Return False if the size of both images is not the same
		"""
		
		if (first_image.get_size_KB_image() == second_image.get_size_KB_image()):
			self.is_image_size_the_same = True
		else:
			self.is_image_size_the_same = False
		
		return self.is_image_size_the_same
		