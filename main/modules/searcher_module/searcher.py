class Searcher:
	
	def __init__(self, search_type):
		self.search_type = search_type
		
	def search_duplicates(self, list_of_images_to_look_for):
		""" Call the search of the specific type
		
		"""
		name_of_images_duplicated = self.search_type.search_duplicates(list_of_images_to_look_for)
		return name_of_images_duplicated
	
	def change_search_type(self, seacrh_type):
		self.search_type = search_type