from javax.imageio import *
from java.awt import *
from java.awt.image import *
from java.io import *
from java.lang.Math import *
import sys
sys.path.append("../../../")
from  modules.logger_module.logger import  Logger

class ManagerImage:
    logger_file = Logger()

    def resize_image(self,input_file, width, height,type_image):
        """ Modify image with new sizes in pixels 

        Keyword arguments:
        width: new width size to image 
        height_image: new height size to image

        """

        # Get the BufferedImage object by reading the image from the given input stream
        buffered_image = ImageIO.read(FileInputStream(input_file))

        # I am using fast scaling
        resized_img = buffered_image.getScaledInstance(width, height, Image.SCALE_DEFAULT)

        # Create a BufferedImage object with the width and height and of the image type
        buffered_image_type = BufferedImage(width, height, buffered_image.getType())

        # Create Graphics object
        img_graphics = buffered_image_type.createGraphics()

        # Draw the resizedImg from 0,0 with no ImageObserver
        img_graphics.drawImage(resized_img, 0, 0, None)

        # Dispose the Graphics object, we no longer need it
        img_graphics.dispose()

        # The first argument is the resized image object
        # The second argument is the image file type, So i got the extension of the output file and passed it
        # The next argument is the FileOutputStream to where the resized image is to be written.
        ImageIO.write(buffered_image_type_image, type_image , FileOutputStream(output_file))
        self.logger_file.set_info("The image" + input_file + " was resized.")


    def rotate_image(self, input_file, angle, type_image):

        # The first argument is the input file
        # Get the BufferedImage object by reading the image from the given input stream
        image_to_rotate = ImageIO.read(FileInputStream(input_file))


        new_image = BufferedImage(image_to_rotate.getHeight(), image_to_rotate.getWidth(), image_to_rotate.getType())

        graphics = new_image.getGraphics()

        # The first line will rotate the image according the angle especified
        # The second command will change the origin of the new image to stablish as new start point for the rotation
        graphics.rotate(toRadians(angle), new_image.getWidth() / 2, new_image.getHeight() / 2)
        graphics.translate((new_image.getWidth() - image_to_rotate.getWidth()) / 2, (new_image.getHeight() - image_to_rotate.getHeight()) / 2);

        # Draw the image from the 0,0 coordinate until the height and size especified
        graphics.drawImage(image_to_rotate, 0, 0, image_to_rotate.getWidth(), image_to_rotate.getHeight(), None)

        # Dispose the Graphics object, we no longer need it
        graphics.dispose()

        # The first argument is the resized image object
        # The second argument is the image file type, So i got the extension of the output file and passed it
        # The next argument is the FileOutputStream to where the resized image is to be written.
        ImageIO.write(image_to_rotate, type_image, FileOutputStream(input_file))
        self.logger_file.set_info("The image" + input_file + " was rotated")


    def size_width(self, input_file):

        # The first argument is the input file
        # Get the BufferedImage object by reading the image from the given input stream
        image_info = ImageIO.read(FileInputStream(input_file))
        return image_info.getWidth()

    def size_height(self, input_file):

        # The first argument is the input file
        # Get the BufferedImage object by reading the image from the given input stream
        image_info = ImageIO.read(FileInputStream(input_file))
        return image_info.getHeight()

    def convert_image(self, input_file, output_file, new_format):
        """
        Convert the image to other format
        Keyword arguments:
		input_file: original image file
                output_file: new image file
                new_format: format of image
        """
        
        # Get the BufferedImage object by reading the image from the given input stream
        buffered_image = ImageIO.read(FileInputStream(input_file))
        #/ create a blank, RGB, same width and height, and a white background
	newBufferedImage = BufferedImage(buffered_image.getWidth(),
			buffered_image.getHeight(), BufferedImage.TYPE_INT_RGB)
	newBufferedImage.createGraphics().drawImage(buffered_image, 0, 0, Color.WHITE, None)
        newBufferedImage.createGraphics().dispose()

	#write to type file
	ImageIO.write(newBufferedImage, new_format, FileOutputStream(output_file))