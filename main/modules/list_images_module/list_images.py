import os
import sys
import os.path

#sys.path.append("..")
from main.modules.searcher_module.searcher import Searcher

class ListImages():
	"""Class ListImages handles the files retrieved from a given path and add them to an array"""
	
	images = [] 
	image_file_types = [] # The supported file types 
	
	
	def __init__(self):
		self.image_file_types = ['.jpg', '.png', '.bmp']
	
	def is_file_in_image_scope(self, extension):
		"""Verify extension is contained in files supported and return a True/False 
		
		Keyword arguments:
		extension -- A string  value that represents the extension of a file. This can be '.jpg' or '.txt'		
		
		Returned value:
		is_supported_format -- Boolean value. True if extension is in the pre-defined list of supported formats
		
		"""
		
		is_supported_format = False
		if extension in self.image_file_types:
			is_supported_format = True
		
		return is_supported_format
		
		
	def get_all_images_from_directory(self, size, list_of_images, list_of_directories):
		"""Add all images contained in the list of directories received to a list and and returns that list.
			It receives a list of directories and in a recursive way list all images contained on those.
			
		Keyword arguments:
		size -- Int value that represents the current size of the elements not visited yet. 
				Initial value will be the same as the lenght of the list of directories received 
				
		list_of_images -- The list of images collected from the directories. 
							This will grow with each recursive call to the method
							
		list_of_directories -- The list of all directories where it needs to look for. 
								This list will be the same always.
		
		
		Returned value: The list of images found in the list_of_directories specified
		
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
		given_path -- String value that represent the absolute path of the top level folder we want to 
					extract the list of folders. i.e.: If we have the below tree
					D:/
						/images
							/personal images
								/photos
									/draws
					If we want images from personal images and nested directoriesit would be 'D:/images/personal images'
		
		Returned value:
		list_of_directories_full_path -- A list that contains the full path of each directory found
										This list also includes the top level path given as argument.
									With above example we will have the below list returnes
									list_of_directories_full_path = ['D:/images/personal images',
																	'D:/images/personal images/photos',
																	'D:/images/personal images/photos/draws',
		
		"""
		
		if (given_path == ''):
			given_path = os.path.expanduser('~')
		
		print given_path
		
		list_of_directories_full_path = []
		for root, dirs, files in os.walk(given_path):
			list_of_directories_full_path.append(root)
		
		return list_of_directories_full_path
	
	def search_images_in_path(self, path, search_type, size, list_of_images, list_of_directories):
		"""Defines the path, the strategy where the search will be performed and returns all the images
		   duplicated in a list
		
		"""
	
		list_of_images_from_path = self.get_all_images_from_directory(size, list_of_images, list_of_directories)
		searcher = Searcher(search_type);
		list_of_duplicated_images = searcher.search_duplicates(list_of_images_from_path);
		return list_of_duplicated_images;
		