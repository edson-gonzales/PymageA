import sys
import os
sys.path.append("../../../src/")
from modules.logger_module.logger import Logger

class GeneralSearch():
	
	def __init__(self):
		""" Initialize the GeneralSearch with an empty list of duplicates by default
		"""
		self.list_of_duplicates = []
                self.logger_file = Logger()
		
	def search_duplicates(self, list_of_images_to_look_for):
		"""Search duplicated images by the comparison method implemented and return all the equal 
		items in a list. This list contains a list of ImageFile objects
			
		Keyword arguments:
		list_of_images_to_look_for -- The list of ImageFile objects where we are going to search
									equal images taking as criteria the size
		Returned values:
		list_of_duplicates -- The list of ImageFiles that are equal
		
		""" 
		
		list_to_compare = list_of_images_to_look_for
                try:
                    for image_object in list_of_images_to_look_for:
                            num_of_copies = 0
                            for image_object_compare in list_to_compare:
                                    if (self.comparison_criteria(image_object_compare, image_object)):
                                            num_of_copies = num_of_copies + 1
                            if num_of_copies > 1:
                                    self.list_of_duplicates.append(image_object)
                except:
                	exception_type = str(sys.exc_info()[0])
                	message_exception= str(sys.exc_info()[1])
                	self.logger_file.set_exception(exception_type,message_exception)
                    
		return self.list_of_duplicates	
	
	def comparison_criteria(self, first_image, second_image):
		""" This method should be implemented by the children classes 
		"""
		raise Exception
		exception_type = str(sys.exc_info()[0])
		message_exception= str(sys.exc_info()[1])
		self.test_logger.set_exception(exception_type,message_exception)
	
	def show_path_of_duplicated_images(self):
		""" Prints on console the path of each image duplicated found
		"""
		for image_duplicated in self.list_of_duplicates:
			print "The images ", image_duplicated.get_full_path_with_name_image_type()
	
	