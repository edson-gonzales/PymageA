from general_search import GeneralSearch

class SearchDuplicatesBySize(GeneralSearch):
	
	def search_duplicates(self, list_of_images_to_look_for):
		"""Search duplicated images by size and return all the equal items in a list.
			This list contains a list of ImageFile objects
			
		Keyword arguments:
		list_of_images_to_look_for -- The list of ImageFile objects where we are going to search
									equal images taking as criteria the size
		Returned values:
		list_of_duplicates -- The list of ImageFiles that are equal
		
		""" 
		
		list_to_compare = list_of_images_to_look_for
		for image_object in list_of_images_to_look_for:
			num_of_copies = 0
			for image_object_compare in list_to_compare:
				if image_object_compare.get_size_KB_image() == image_object.get_size_KB_image():
					num_of_copies = num_of_copies + 1
			if num_of_copies > 1:
				self.list_of_duplicates.append(image_object)
		
		return self.list_of_duplicates	