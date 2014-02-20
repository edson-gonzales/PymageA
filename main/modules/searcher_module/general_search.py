class GeneralSearch():
	
	def __init__(self):
		""" Initialize the GeneralSearch with an empty list of duplicates by default
		"""
		self.list_of_duplicates = []
		
	def search_duplicates(self, list_of_images_to_look_for):
		""" Search duplicated images. This should be implemented by the children classes 
		"""
		raise Exception
	
	def show_path_of_dupicated_images(self):
		""" Prints on console the path of each image dupliactes found
		"""
		for image_duplicated in self.list_of_duplicates:
			print image_duplicated.get_full_path_with_name_image_type()
		