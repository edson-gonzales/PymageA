from java.awt import Canvas
class ShowImage (Canvas):
    """
    Class to display the image selected in JList, it is displaye in south pane
    """
    def ShowImage(self, img):
        """
        Construnctor of class
        """
        Canvas.__init__(self)
        self.img = img
    def paint (self, g):
        """
        Draw the image with specific size
        """
        if(self.img != None):
            g.drawImage(self.img, 0, 0, 300, 300, self)

    def setImage (self, img):
        self.img = img


