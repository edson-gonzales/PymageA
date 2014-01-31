import os

class ListImages():
	images = [] 
	
	def get_all_images_from_path(self, given_path):
		list_of_files = os.listdir(given_path)
		return list_of_files


		