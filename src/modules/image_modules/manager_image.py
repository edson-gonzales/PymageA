from javax.imageio import *
from java.awt import *
from java.awt.image import *
from java.io import *
from java.lang.Math import *
from javax.swing import JLabel
from java.awt import Graphics
from java.awt import Image
from  java.awt import Component
class ManagerImage:

    def resize_image(self,input_file, width, height,type_image):
        """ Modify image with new sizes in pixels 

        Keyword arguments:
        width: new width size to image 
        height_image: new height size to image

        """
        input_file1 = "c:\Users\mitest.jpg"
        # Get the BufferedImage object by reading the image from the given input stream
        buffered_image = ImageIO.read(FileInputStream(input_file))

        # I am using fast scaling
        resized_img = buffered_image.getScaledInstance(width, height, Image.SCALE_DEFAULT)
        print "mis heig and wirf",width, height, type_image
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
        print "soy inpu file",input_file
        ImageIO.write(buffered_image_type, type_image , FileOutputStream(input_file1))


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

    def drawScaledImage(self, image, canvas, g):
        imgWidth = image.getWidth(None)
        imgHeight = image.getHeight(None)
        imgAspect = float(imgHeight / imgWidth) #double
        canvasWidth = canvas.getWidth()
        canvasHeight = canvas.getHeight()
        canvasAspect = float(canvasHeight / canvasWidth)
        x1 = 0 # top left X position
        y1 = 0 # top left Y position
        x2 = 0 # bottom right X position
        y2 = 0 # bottom right Y position
        if (imgWidth < canvasWidth and imgHeight < canvasHeight):
            # the image is smaller than the canvas
            x1 = (canvasWidth - imgWidth)  / 2
            y1 = (canvasHeight - imgHeight) / 2
            x2 = imgWidth + x1
            y2 = imgHeight + y1
        else:
            if (canvasAspect > imgAspect):
                y1 = canvasHeight
                # keep image aspect ratio
                canvasHeight = int ((canvasWidth * imgAspect))
                y1 = (y1 - canvasHeight) / 2
            else:
                x1 = canvasWidth
                #keep image aspect ratio
                canvasWidth = int(canvasHeight / imgAspect)
                x1 = (x1 - canvasWidth) / 2
            x2 = canvasWidth + x1
            y2 = canvasHeight + y1
        
        g.drawImage(image, x1, y1, x2, y2, 0, 0, imgWidth, imgHeight, None)

