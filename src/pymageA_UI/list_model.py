from javax.swing import AbstractListModel
from javax.swing import DefaultListCellRenderer
from javax.swing import ListCellRenderer
from javax.swing import ImageIcon

class GeneratedListModel (AbstractListModel):
    """
    Define the list model to use, using images
    """
    def __init__(self):
 	    #self.panelA = panelA
            AbstractListModel.__init__(self)
            self.image_founds = []
    def addImage(self,image_object):
        self.image_founds.append(image_object)
        
    def getSize(self):
        return len(self.image_founds)

    def update(self):
        self.fireContentsChanged(self, 0,self.getSize())

