from javax.imageio import *
from java.awt import *
from java.awt.image import *
from java.io import *
from java.lang.Math import *
import sys
sys.path.append("../../../src")
from  modules.logger_module.logger import  Logger

class ManagerImage:
    logger_file = Logger()

    def resize_image(self, input_file, width, height, type_image):
        """ Modify image with new sizes in pixels 

        Keyword arguments:
        input_file: name of file to resize the image
        width: new width size to image
        height_image: new height size to image
        type_image = type of image 

        """
        buffered_image = ImageIO.read(FileInputStream(input_file))
        resized_img = buffered_image.getScaledInstance(width, height, Image.SCALE_DEFAULT)
        buffered_image_type = BufferedImage(width, height, buffered_image.getType())
        img_graphics = buffered_image_type.createGraphics()
        img_graphics.drawImage(resized_img, 0, 0, None)        
        type_image = type_image.strip('.')
        output_file_stream =FileOutputStream(input_file)
        ImageIO.write(buffered_image_type, type_image, output_file_stream)
        output_file_stream.close()        
        self.logger_file.set_info("The image was resized.")


    def rotate_image(self, input_file, angle, type_image):
        """ Modify image with angle

        Keyword arguments:
        input_file: name of file to rotate
        anlge: angle to rotate
        type_image = type of image

        """        
        image_to_rotate = ImageIO.read(FileInputStream(input_file))
        new_image = BufferedImage(image_to_rotate.getHeight(), image_to_rotate.getWidth(), image_to_rotate.getType())
        graphics = new_image.getGraphics()
        graphics.rotate(toRadians(angle), new_image.getWidth() / 2, new_image.getHeight() / 2)
        graphics.translate((new_image.getWidth() - image_to_rotate.getWidth()) / 2, (new_image.getHeight() - image_to_rotate.getHeight()) / 2);
        graphics.drawImage(image_to_rotate, 0, 0, image_to_rotate.getWidth(), image_to_rotate.getHeight(), None)
        graphics.dispose()
        type_image = type_image.strip('.')
        output_file_stream =FileOutputStream(input_file)
        ImageIO.write(new_image, type_image, output_file_stream)
        output_file_stream.close()
        self.logger_file.set_info("The image" + input_file + " was rotated")


    def size_width(self, input_file):
        """ Get the size (width in pixels) of image

        Keyword arguments:
        input_file: name of file

        """
        image_info = ImageIO.read(FileInputStream(input_file))
        return image_info.getWidth()

    def size_height(self, input_file):
        """ Get the size (height in pixels) of image
        Keyword arguments:
        input_file: name of file

        """        
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
        buffered_image = ImageIO.read(FileInputStream(input_file))        
	newBufferedImage = BufferedImage(buffered_image.getWidth(),
			buffered_image.getHeight(), BufferedImage.TYPE_INT_RGB)
	newBufferedImage.createGraphics().drawImage(buffered_image, 0, 0, Color.WHITE, None)
        newBufferedImage.createGraphics().dispose()	
	ImageIO.write(newBufferedImage, new_format, FileOutputStream(output_file))