from general_search import GeneralSearch

class SearchDuplicatesByName(GeneralSearch):
	
	def search_duplicates(self, list_of_images_to_look_for):
		"""Search duplicated images by name and return the name in a list
		
		"""
		list_of_duplicates = []
		for image_object in list_of_images_to_look_for:
			for image_object_compare in list_of_images_to_look_for:
				num_of_copies = 0
				if image_object_compare.get_complete_image_with_type() == image_object.get_complete_image_with_type():
					num_of_copies = num_of_copies + 1
			if num_of_copies > 1:
				list_of_duplicates.append(image_object_compare)
				
		return list_of_duplicates
	