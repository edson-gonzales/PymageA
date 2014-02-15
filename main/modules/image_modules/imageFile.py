import imghdr
import Image
import os
import sys
import platform



class ImageFile():
	"""Class ImageFile handles the image files, all operation to image file are described in it"""
	file_name =''
	file_size = ''
	file_owner = ''
	file_type = ''
	file_path = ''
	file_size_high = ''
	file_size_width = ''
	file_image_full_path = ''
	image_file_type = ['JPG','BMP','PNG']  # The supported file types 
	size_KB_image = ' '

	def __init__(self):
		self.file_path = "" #root path by default-windows
		self.max_size = 1000
		self.min_size = 1
		

	def verify_image_values(self, full_path_file_image, full_name_file_image): 
		"""verify if path and name are valid and set the values in object ImageFile 
		 	
		Keyword arguments:
		
		full_path_file_image -- path of image
		full_name_file_image -- file name image

		Return Value:
		True -- if the values in object were set correctly 
		False -- If the object is not a image file and the values are not set
		"""
		if full_path_file_image.endswith('/') == False and full_path_file_image.endswith('\\') == False:
			full_path_file_image = full_path_file_image + '/'
		if (self.is_valid_image(full_path_file_image, full_name_file_image) == True):

			split_name_image = os.path.splitext(full_name_file_image)	
			file_name_image = split_name_image[0]
			file_type_image = split_name_image[1].translate(None, '.')#remove . from extension file
			self.file_path = os.path.abspath(full_path_file_image)
			self.file_name = file_name_image
			self.file_type = file_type_image
			image_full_path_name = os.path.abspath(full_path_file_image + full_name_file_image)
			self.file_image_full_path = image_full_path_name
			new_image = Image.open(image_full_path_name)
			info_file_image = os.stat(image_full_path_name)
			self.size_KB_image = info_file_image.st_size #size of image file
			self.set_size_pixels(new_image.size[1], new_image.size[0])
			self.set_file_onwer(full_path_file_image, full_name_file_image)			
			return True
		return False

	def set_file_onwer(self, full_path_file_image, full_name_file_image):
		if (platform.system() == "Linux"):
			self.set_file_owner_in_platform_linux(full_path_file_image, full_name_file_image)
		if platform.system() == 'Windows' :
			self.set_file_owner_in_platform_Windows(full_path_file_image, full_name_file_image)
		

	def set_file_owner_in_platform_linux(self, full_path_file_image, full_name_file_image):
		""" Set owner to imageFile  when project is running in platform Linux

		Keyword arguments:
		full_path_file_image -- path were image is located
		full_name_file_image -- file name image (with extension) 
		"""
		image_full_path_name = os.path.abspath(full_path_file_image + full_name_file_image)
		info_file_image = os.stat(image_full_path_name)
		uid = info_file_image.st_uid
		self.file_owner = pwd.getpwuid(uid).pw_name

	def set_file_owner_in_platform_Windows(self, full_path_file_image, full_name_file_image):
		""" Set owner to imageFile  when project is running in platform Windows

		Keyword arguments:
		full_path_file_image -- path were image is located
		full_name_file_image -- file name image (with extension) 

		"""
		if full_path_file_image.endswith('/') == True or full_path_file_image.endswith('\\') == True:
				full_path_file_image = full_path_file_image[:-1]
		full_path_file_image = os.path.abspath(full_path_file_image)
		mypath = os.path.dirname(os.path.abspath(__file__))
		new_name = os.path.dirname(os.path.abspath(__file__)) + '/delete' + full_name_file_image + '.txt'
		new_name = os.path.abspath (new_name)
		command_windows = 'dir /q ' + full_path_file_image + '\\' + full_name_file_image + '>' + new_name
		info_file = os.system(command_windows)
		try:
			file_info = open(new_name)
			lines = file_info.readlines()
			info_file_owner = (lines[5].rstrip("\n")).split(' ')
			self.file_owner = (info_file_owner[len(info_file_owner)-2]).split("\\")
			file_info.close()
			os.remove(new_name)
		except IOError:
				print("File cannot open" + new_name)


	def is_valid_image(self,full_path_file_image,full_name_file_image):
		"""Validate the image file and path and return a True/False 
		
		Keyword arguments:
		
		full_path_file_image -- path of image
		full_name_file_image -- file name image

		Return Value:
		True -- if image file is a valid image: exist and type image is supported by ImageFile
		False -- If the image file is not valid: the file doesn't exist or 
				 type image is not supported by ImageFile
		"""
		full_path_image = full_path_file_image + full_name_file_image
		if os.path.isfile(full_path_image):#file exist		
			split_name_image = os.path.splitext(full_name_file_image)	
			file_type_image = split_name_image[1].translate(None, '.')
			if (self.is_image_type_valid(file_type_image)) == True: 
				return True
		return False


	def get_complete_image_with_type(self):
		"""Return the name and extension of image"""
		return (self.get_name() + "." + self.get_type())

	def get_full_path_with_name_image_type(self):
		"""Return location(path) and name.extension of image"""
		return (os.path.join(self.get_path(),self.get_complete_image_with_type()))

	def get_file_name(self):
		"""Return name of imageFile"""
		return self.file_name

	def set_file_name(self, file_name_image):
		""" Set name to imageFile
		Keyword arguments:
		file_name image-- filename of image file
		
		 """
		self.file_name = file_name_image

	def set_size_pixels(self, size_high_image, size_width_image):
		""" Set dimensions to imageFile

		Keyword arguments:
		size_high_image-- high image file
		size_witdh_image-- width image file
		
		 """
		self.file_size_high = size_high_image
		self.file_size_width = size_width_image

	def get_file_size_high(self):
		"""Return size(high) of imageFile"""
		return self.file_size_high

	def get_file_size_width(self):
		"""Return size(with in pixels) of imageFile"""
		return self.file_size_width

	
	def get_file_owner(self):
		"""Return owner of imageFile"""
		return self.file_owner


	def set_size_KB_image(self, size_image_KB):
		""" Set sizein KB to imageFile
		
		Keyword arguments:
		size_image_KB-- size in KB of image file
		
		"""
		self.size_KB_image = size_image_KB

	def get_size_KB_image(self):
		"""Return size in KB of imageFile"""
		return self.size_KB_image


	def get_file_type(self):
		"""Return type of imageFile"""
		return self.file_type

	def set_file_type(self, file_type_image):
		""" Set type to imageFile
		
		Keyword arguments:
		file_type_image-- type of image file
		
		"""
		self.file_type = file_type_image

	
	def set_file_path(self, file_path_image):
		""" Set path to imageFile
		
		Keyword arguments:
		file_path_image-- path were image is located
		
		"""
		self.file_path = file_path_image

	def get_file_path(self):
		"""Return path of imageFile"""
		return self.file_path

	def is_image_type_valid(self, type_file):
		"""Verify if type is a type permitted to imageFile
		Return 
			True: if type image is type permitted
			False: if type image is not permitted
		"""
		if (type_file.upper() in self.image_file_type):
			return True
		return False
	
	def resize_image(self, new_high_image, new_width_image):
		"""Modify image with new sizes in pixels if the parameters (new_width_image,new_high_image) are valid

		Keyword arguments:
		new_width_image: new width size to image 
		new_high_image: new high size to image

		Return
		True: If new sizes are valid and the image is resized
		False: If new sizes are not valid and the image is not resized
		"""
		if (self.is_valid_size_image(new_width_image, new_high_image) == True):
			image_Change_size = Image.open(self.file_image_full_path)
			image_Change_size = image_Change_size.resize((new_width_image, new_high_image), Image.ANTIALIAS)
			image_Change_size.save(os.path.abspath(self.file_image_full_path))
			return True
		return False

	def is_valid_size_image(self, new_width_image, new_high_image):
		""" Verify if the sizes (with and height) are in proper range : 1..1000 
		Keyword arguments
		new_high_image : new high size to image
		new_width_image: new high size to image
		
		Return
		True: if the new sizes are valid and are in proper range
		False: If the new size are not valid
		"""
		if ((self.min_size < new_width_image <= self.max_size) and type(new_width_image) == int) and \
			 ((self.min_size < new_high_image <= self.max_size) and type(new_high_image) == int):
			
			return True
		return False

	def rotate_image(self, angle_to_rotate):
		"""Modify image with new angle
		Keyword arguments:		
		angle_to_rotate: angle to rotate the image
		
		Return
		True: if the image is rotate with angle_to_rotate
		False: If the image is not rotate

		"""
		if (self.is_valid_angle_image(angle_to_rotate)):
			image_rotate = Image.open(self.file_image_full_path)
			image_rotate = image_rotate.rotate(angle_to_rotate)
			image_rotate.save(self.file_image_full_path)
			return True

		return False




	def is_valid_angle_image(self, angle):
		""" Verify if the angle is a integer value and is in proper range: 0 ..180
		Return
		True: if the angle is valid
		False: if the angle is not valid

		"""
		if (-180 <= angle <=180 and type(angle) == int):
			return True
		return False
