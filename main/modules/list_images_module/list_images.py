import os

class ListImages():
	"""Class ListImages handles the files retrieved from a given path and add them to an array"""
	
	images = [] 
	image_file_types = [] # The supported file types 
	
	
	def __init__(self):
		self.image_file_types = ['.jpg', '.png', '.bmp']
	
	def is_file_in_image_scope(self, extension):
		"""Verify extension is contained in files supported and return a True/False 
		
		Keyword arguments:
		extension -- Given extension of a file
		
		"""
		
		it_is = False
		if extension in self.image_file_types:
			it_is = True
		
		return it_is
		
		
	def get_all_images_from_directory(self, size, list_of_images, list_of_directories):
		"""Add all images contained in the list of directories received to a list and and returns that list.
			It receives a list of directories and in a recursive way list all images contained on those.
			
		Keyword arguments:
		size -- The current size of the elements not visited yet. 
				Initial value will be the same as the lenght of the list of directories received 
		list_of_images -- The list of images collected from the directories. 
							This will grow with each recursive call to the method
		list_of_directories -- The list of all directories where it needs to look for. 
								This list will be the same always. 
		
		"""
		
		next_folder_in_array = len(list_of_directories) - size # To step up on each position of the directory list 
		if next_folder_in_array >= len(list_of_directories):
			return list_of_images
		else:
			list_of_files = os.listdir(list_of_directories[next_folder_in_array])
			size = size - 1
			for file_name in list_of_files:
				file_base_name, file_extension = os.path.splitext(file_name)
				if self.is_file_in_image_scope(file_extension):
					list_of_images.append(file_name)
					
			return (self.get_all_images_from_directory(size, list_of_images, list_of_directories))
		
	def get_all_nested_directories(self, given_path):
		""" Retrieves all nested directories from a path and return them in a list
			
		Keyword arguments:
		given_path -- The top level folder we want to extract the list of folders.
		
		"""
		
		list_of_directories_full_path = []
		for root, dirs, files in os.walk(given_path):
			list_of_directories_full_path.append(root)
		
		return list_of_directories_full_path
	
	
		