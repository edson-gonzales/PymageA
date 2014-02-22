from general_search import GeneralSearch

class SearchDuplicatesByName(GeneralSearch):
	
	def comparison_criteria(self, first_image, second_image):
		""" Compare if the name is the same for two images given
			
		Keyword arguments:
		first_image -- An ImageFile object that will be compared with secon_image
		second_image -- An ImageFile object that will be compared with first_image
		
		Returned values:
		is_image_size_the_same -- It will Return True if the name of both images is the same
								It will Return False if the name of both images is not the same
		"""
		
		if (first_image.get_complete_image_with_type() == second_image.get_complete_image_with_type()):
			self.is_image_name_the_same = True
		else:
			self.is_image_name_the_same = False
		
		return self.is_image_name_the_same
				