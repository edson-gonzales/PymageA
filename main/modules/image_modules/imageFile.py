import imghdr
import os
class ImageFile():
	"""Class ImageFile handles the image files, all operation to image file are described in it"""
	file_name=''
	file_size=''
	file_owner=''
	file_type=''
	file_path=''
	file_size_high=''
	file_size_width=''
	image_file_type=['JPG','BMP','PNG']  # The supported file types 


	def __init__(self):
		self.file_path="" #root path by default-windows

	def set_image_values(self,full_path_file_image,full_name_file_image): 
		"""Set the values to imageFile if the file image and path are valid and return a True/False 
		
		Keyword arguments:
		
		full_path_file_image -- path of image
		full_name_file_image -- file name image
		"""
		if full_path_file_image.endswith('/')==False:
			full_path_file_image=full_path_file_image+'/'
		if (self.validate_image(full_path_file_image,full_name_file_image)==True):
			split_name_image=os.path.splitext(full_name_file_image)	
			file_name_image=split_name_image[0]
			file_type_image=split_name_image[1].translate(None,'.')#remove . from extension file
			self.set_path(os.path.abspath(full_path_file_image))
			self.set_name(file_name_image)
			self.set_type(file_type_image)
			info_file_image=os.stat(full_path_file_image+full_name_file_image)
			self.file_owner=info_file_image.st_uid #uid owner of file image
			return True
		return False


	def validate_image(self,full_path_file_image,full_name_file_image):
		"""Validate the image file and path and return a True/False 
		
		Keyword arguments:
		
		full_path_file_image -- path of image
		full_name_file_image -- file name image
		"""
		full_path_image=full_path_file_image+full_name_file_image
		if os.path.isfile(full_path_image):#file exist		
			split_name_image=os.path.splitext(full_name_file_image)	
			file_type_image=split_name_image[1].translate(None,'.')
			if (self.validate_type_image(file_type_image))==True: 
				return True
			return False

	def get_complete_image_with_type(self):
		"""Retrieve name and type image"""
		return (self.get_name()+"."+self.get_type())

	def get_full_path_with_name_image_type(self):
		"""Retrieve location(path) and name of image"""
		return (os.path.join(self.get_path(),self.get_complete_image_with_type()))

	def get_name(self):
		"""Retrieve only name of imageFile"""

		return self.file_name

	def set_name(self,file_name_image):
		""" Set name to imageFile
		Keyword arguments:
		file_name image-- filename of image file
		
		 """
		self.file_name=file_name_image

	def set_size(self, size_high_image,size_width_image):
		""" Set dimensions to imageFile

		Keyword arguments:
		size_high_image-- high image file
		size_witdh_image-- width image file
		
		 """
		self.file_size_high=size_high_image
		self.file_size_width=size_width_image

	def get_size_high(self):
		"""Retrieve size(high) of imageFile"""
		return self.file_size_high

	def get_size_width(self):
		"""Retrieve size(with in pixels) of imageFile"""
		return self.file_size_width

	def set_owner(self,owner_file_image):
		""" Set owner to imageFile
		
		Keyword arguments:
		owner_file_image-- owner image file
		
		"""
		self.file_owner

	def get_owner(self):
		"""Retrieve owner of imageFile"""
		return self.file_owner

	def get_type(self):
		"""Retrieve type of imageFile"""
		return self.file_type

	def set_type(self,file_type_image):
		""" Set type to imageFile
		
		Keyword arguments:
		file_type_image-- type of image file
		
		"""
		self.file_type=file_type_image

	
	def set_path(self,file_path_image):
		""" Set path to imageFile
		
		Keyword arguments:
		file_path_image-- path were image is located
		
		"""
		self.file_path=file_path_image

	def get_path(self):
		"""Retrieve owner path imageFile"""
		return self.file_path

	def validate_type_image(self,type_file):
		"""Verify if type is a type permitted to imageFile and return True/False"""
		if (type_file.upper() in self.image_file_type):
			return True
		return False
	




