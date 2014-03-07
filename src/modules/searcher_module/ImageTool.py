# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="egonzales"
__date__ ="$Feb 21, 2014 12:28:11 PM$"

import os
import math
from java.awt import *
from java.awt.image import *
from javax.swing import *
from java.io import *
from javax.imageio import *

class ImageCalculator:
    _image = None
    size = 0
    image_width = 0
    image_height = 0
    #
    # Constructs a Histogram for an image.
    #
    def __init__(self, input_path):
        buffered_image = ImageIO.read(FileInputStream(input_path))
	self._image = buffered_image
	self.size = os.stat(input_path)
        self.image_width = self._image.getWidth(None)
	self.image_height = self._image.getHeight(None)
		
    def get_image(self):
	return self._image

    def get_pixels(self):
	iw = self._image.getWidth(None)
	ih = self._image.getHeight(None)
	pixels = [[0 for x in xrange(ih)] for x in xrange(iw)]
	if (self._image.getType() == 10):
            data_buffer = self._image.getRaster().getDataBuffer()
            pixel_array = data_buffer.getData()
            for x in range(iw):
                for y in range(ih):
                    pixels[x][y] = pixel_array[x + y * iw]
	elif(self._image.getType() == 11):
            data_buffer = image.getRaster().getDataBuffer()
            pixel_array = data_buffer.getData()
            for x in range(iw):
                for y in range(ih):
                    pixels[x][y] = pixel_array[x + y * iw]
	return pixels


    def get_histogram(self) :
	histogram = None
	if self._image.getType() == 10:
            histogram = [0 for x in xrange(256)]
	else:
            histogram = [0 for x in xrange(2001)];
	pixels = self.get_pixels()
	for x in range(len(pixels)):
            for y in range(len(pixels[0])):
                histogram[pixels[x][y]] += 1
            
	return histogram


def rmsdiff_2011(image_a, image_b):
	"Calculate the root-mean-square difference between two images"
	histogram_a = image_a.get_histogram()
	histogram_b = image_b.get_histogram()
	hist_diff = [0 for x in xrange(len(histogram_b))]
	for i in range(len(histogram_a)):
		hist_diff[i] = abs(histogram_a[i] - histogram_b[i])

	sq = (value**2 for idx, value in enumerate(hist_diff))
	sum_of_squares = sum(sq)
	rms = math.sqrt(sum_of_squares/float(image_a.image_width * image_a.image_height))
	return rms

#
# Method that compares using the histograms
#
def histogram_compare(image_a, image_b, alpha = .01):
    if image_a.size == image_b.size :
        histogram_a = image_a.get_histogram()
        histogram_b = image_b.get_histogram()

        sum_image_mode_a = 0.0
        sum_image_mode_b = 0.0

	difference_modes = 0.0

	for i in range(len(histogram_a)):
            sum_image_mode_a += histogram_a[i]
            sum_image_mode_b += histogram_b[i]
	    difference_modes += abs(histogram_a[i] - histogram_b[i])

	max_sum = max(sum_image_mode_a, sum_image_mode_b)
	if difference_modes > alpha * max_sum:
            return False
	return True
    return False
