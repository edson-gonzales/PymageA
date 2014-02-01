import imghdr
import os
class image_file:
	file_name=''
	file_size=''
	file_owner=''
	file_type=''
	file_path=''
	file_size_high=''
	file_size_width=''


	def __init__(self):
		self.file_path="" #root path by default-windows

	def set_image_values(self,full_path_file_image,full_name_file_image): 
		self.set_path(os.path.abspath(full_path_file_image))
		split_name_image=os.path.splitext(full_name_file_image)
		self.set_name(split_name_image[0])
		self.set_type(split_name_image[1].translate(None,'.'))#remove . from extension file


	def get_complete_image_with_type(self):
		return (self.get_name()+"."+self.get_type())

	def get_full_path_with_name_image_type(self):
		return (os.path.join(self.get_path(),self.get_complete_image_with_type()))

	def get_name(self):
		return self.file_name

	def set_name(self,file_name_image):
		self.file_name=file_name_image

	def set_size(self, size_high_image,size_width_image):
		self.file_size_high=size_high_image
		self.file_size_width=size_width_image

	def get_size_high(self):
		return self.file_size_high

	def get_size_width(self):
		return self.file_size_width

	def set_owner(self,owner_file_image):
		self.file_owner

	def get_owner(self):
		return self.file_owner

	def get_type(self):
		return self.file_type

	def set_type(self,file_type_image):
		self.file_type=file_type_image

	
	def set_path(self,file_path_image):
		self.file_path=file_path_image

	def get_path(self):
		return self.file_path

	def get_full_file_name(self):
		return self.file_path+"\\"+self.file_name+"."+self.file_type

	def is_image_PNG(self):
		if((imghdr.what(self.get_full_file_name()))).upper()=="PNG":
			return True
		else:
			return False

	




