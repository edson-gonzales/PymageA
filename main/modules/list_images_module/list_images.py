import os

class ListImages():
	"""Class ListImages handles the files retrieved from a given path and add them to an array"""
	
	images = [] 
	image_file_types = [] # The supported file types 
	
	def __init__(self):
		self.image_file_types = ['.jpg', '.png', '.bmp']
	
	def is_file_in_image_scope(self, extension):
		"""Verify extension is contained in files supported and return a True/False """
		
		it_is = False
		if extension in self.image_file_types:
			it_is = True
		return it_is
			
		
	def get_all_images_from_directory(self, size, list_of_images, list_of_directories):
		"""Add all images contained in directories and subdirectories to a list and returns the list"""
		
		#list_of_directories = self.get_all_nested_directories(given_path) 
		#list_of_images = []
		next_folder_in_array = len(list_of_directories) - size
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
		""" Retrieves all nested directories from a path and return them in a list"""
		
		list_of_directories_full_path = []
		for root, dirs, files in os.walk(given_path):
			list_of_directories_full_path.append(root)
		return list_of_directories_full_path
	
	
		