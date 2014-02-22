from javax.swing import AbstractListModel
from javax.swing import DefaultListCellRenderer
from javax.swing import ListCellRenderer
from javax.swing import ImageIcon

class GeneratedListModel (AbstractListModel):
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

class ImageRenderer (ListCellRenderer):
    def getListCellRendererComponent(self, list,image_found,index, isSelected, cellHasFocus):

        ListCellRenderer.__getListCellRendererComponent__(list,image_found,index, isSelected, cellHasFocus)
        position = image_found.get_file_name()
        print"icon sere ",image_found.get_file_name()
        #imageIcon = ImageIcon(getClass().getResource(image_found.get_full_path_with_name_image_type()))
        imageIcon = createImageIcon(image_found.get_file_name(),"")
        setIcon(imageIcon);
        setText(image_found.get_full_path_with_name_image_type())
        return self

