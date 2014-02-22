class Searcher:
	
	def __init__(self, search_type):
		""" Set the search type with an object that will inherit from the General Search class 
		
		Keyword arguments:
		search_type -- The search type we want to set initially. This will be an object that will 
			inherit from GeneralSearch class
		
		"""
		
		self.search_type = search_type
		
	def search_duplicates(self, list_of_images_to_look_for):
		""" Call the search of the specific type
		
		Keyword arguments:
		list_of_images_to_look_for -- A list of image objects that will be examined in order to 
		find duplicates
		
		Returned value:
		name_of_images_duplicated -- It will return the list of names of the images duplicated. 
		For now it returns the same images received
		
		"""
		name_of_images_duplicated = self.search_type.search_duplicates(list_of_images_to_look_for)
		return name_of_images_duplicated
	
	def change_search_type(self, search_type):
		""" Change the type of search to a new one different from the defined initially
		
		Keyword arguments:
		search_type -- The search type we want to change to. This will be an object that will 
			inherit from GeneralSearch class
		
		"""
	
		self.search_type = search_type