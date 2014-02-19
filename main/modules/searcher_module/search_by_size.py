from general_search import GeneralSearch

class SearchDuplicatesBySize(GeneralSearch):
	
	def search_duplicates(self, list_of_images_to_look_for):
		"""Search duplicated images by name and return the name in a list
		
		"""
		list_of_duplicates = []
		list_to_compare = list_of_images_to_look_for
		for image_object in list_of_images_to_look_for:
			num_of_copies = 0
			for image_object_compare in list_to_compare:
				if image_object_compare.get_size_KB_image() == image_object.get_size_KB_image():
					num_of_copies = num_of_copies + 1
			if num_of_copies > 1:
				list_of_duplicates.append(image_object)
		
		return list_of_duplicates
	
	def show_dupes_images_path(self, list_of_images_duplicated):
		"""Search duplicated images by name and return the name in a list
		
		"""
		for image_duplicated in list_of_images_duplicated:
			print image_duplicated.get_full_path_with_name_image_type()
		
		
	