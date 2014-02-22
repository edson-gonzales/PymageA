from general_search import GeneralSearch
import Image
import ImageChops
import math

class SearchDuplicatesByRMS(GeneralSearch):
	
	def comparison_criteria(self, first_image, second_image):
		""" Compare if the size in KB is the same for two images given
			
		Keyword arguments:
		first_image -- An ImageFile object that will be compared with secon_image
		second_image -- An ImageFile object that will be compared with first_image
		
		Returned values:
		is_image_size_the_same -- It will Return True if the size of both images is the same
								It will Return False if the size of both images is not the same
		"""
		
		"Calculate the root-mean-square difference between two images"
		new_image_one = Image.new("RGB", (first_image.get_file_size_width(),first_image.get_file_size_high ()))
		new_image_two = Image.new("RGB",(second_image.get_file_size_width(), second_image.get_file_size_high ()))
		diff = ImageChops.difference(new_image_one, new_image_two)
		h = diff.histogram()
		sq = (value*(idx**2) for idx, value in enumerate(h))
		sum_of_squares = sum(sq)
		rms = math.sqrt(sum_of_squares/float(new_image_one.size[0] * new_image_two.size[1]))
		
		print "The rms value", rms
		
		if (rms < 500):
			self.images_are_the_same = True
		else:
			self.images_are_the_same = False
		
		return self.images_are_the_same
		