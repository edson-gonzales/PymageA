from java.awt import Dimension
from java.awt import GridBagConstraints
from javax.swing import JLabel
from javax.swing import JList
from javax.swing import JPanel
#from pymageA_UI.panel_pymageA import jframe
from modules.image_modules.imageFile import ImageFile
from javax.swing.event import ListSelectionListener
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder
from java.awt import GridBagLayout
from javax.swing import BoxLayout
from javax.swing import Box
from java.awt import Image
from java.io import *
from javax.imageio import *
from java.awt.image import *
from java.awt import Toolkit
from javax.swing import ImageIcon
from image_pymageUI import ScaledImageLabel
from java.awt.event import ActionListener
from modify_image import ModifyImage
from show_image import ShowImage

class JListMouseListener(ListSelectionListener):
    """
    Class to verify the actions that are performent in JList
    """
    
    def __init__(self, jlist,jpanel,list_images,jbutton,jpanel_south):
        self._spacer_panels = Dimension(5, 5)
        ListSelectionListener.__init__(self)
        self.jlist = jlist
        self.jpanel = jpanel
        self.list_images = []
        self.list_images = list_images
        self.jbutton = jbutton
        self.jpanel_south = jpanel_south
        self.show_image = ShowImage(None)
        self.show_image.setSize(300,300);
           
    def updateList(self,list_images):
        """
        update the Jlist where images files are load
        """
        self.list_images = list_images

    def valueChanged(self,event):
        """
        When value in Jlist is changed diferents actions are performed to display
        the details of image selected
        """        
        model = self.jlist.getModel()
        isAdjusting = event.getValueIsAdjusting()        
        if isAdjusting == True:
            if(model.getSize() != 0):
                self.jbutton.setEnabled(True)
            selections = self.jlist.getSelectedIndex()
            selec = model.getElementAt(selections)
            image_selected = ImageFile()
            image_selected = self.list_images[selections]
            element_image = self.jlist.getSelectedValues()
            self.jpanel.removeAll()
            self.jpanel.repaint()
            self.show_details_image(image_selected)
            self.jpanel.revalidate()
        
        

    def show_details_image(self,image_selected):
        """
        Show the details of the image selected in the JList in the south pane
        """
        details_image_text_panel = JPanel()
        details_image_text_panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED), "Details Image"))
        details_image_text_panel.setLayout(GridBagLayout())        
        cConstraints = GridBagConstraints()
        cConstraints.anchor = GridBagConstraints.WEST
        cConstraints.weightx = 0.1
        cConstraints.weighty = 0.1
        self.details_image(details_image_text_panel,cConstraints,image_selected)
        self.jpanel.add(details_image_text_panel)
        image_panel = JPanel()
        image_panel.setLayout(BoxLayout( image_panel, BoxLayout.Y_AXIS))
        image_panel.add(Box.createRigidArea(self._spacer_panels))
        image_panel.add(self.show_image);
        toolkit = Toolkit.getDefaultToolkit()
        image1 = toolkit.getImage(image_selected.get_full_path_with_name_image_type() )
        self.show_image.setImage(image1)
        self.show_image.repaint()
        self.jpanel.add(image_panel)

    def details_image(self, details_image_text_panel,cConstraints,image_selected):
        cConstraints.gridx = 0
	cConstraints.gridy = 0
        details_image_text_panel.add(JLabel("Name"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 0
        details_image_text_panel.add(JLabel(image_selected.get_complete_image_with_type()),cConstraints)
        cConstraints.gridx = 0
	cConstraints.gridy = 1
        details_image_text_panel.add(JLabel("Directory"),cConstraints)
        cConstraints.gridx = 1
	cConstraints.gridy = 1
        details_image_text_panel.add(JLabel(image_selected.get_file_path()),cConstraints)
        cConstraints.gridx = 0
	cConstraints.gridy = 2
        details_image_text_panel.add(JLabel("Owner"),cConstraints)
        cConstraints.gridx = 1
	cConstraints.gridy = 2
        details_image_text_panel.add(JLabel(image_selected.get_file_owner()),cConstraints)
        cConstraints.gridx = 0
	cConstraints.gridy = 3
        details_image_text_panel.add(JLabel("Width(Pixels)"),cConstraints)
        cConstraints.gridx = 1
	cConstraints.gridy = 3
        details_image_text_panel.add(JLabel(str(image_selected.get_file_size_width())),cConstraints)
        cConstraints.gridx = 0
	cConstraints.gridy = 4
        details_image_text_panel.add(JLabel("Height(Pixels)"),cConstraints)
        cConstraints.gridx = 1
	cConstraints.gridy = 4
        details_image_text_panel.add(JLabel(str(image_selected.get_file_size_high())),cConstraints)
        cConstraints.gridx = 0
	cConstraints.gridy = 5
        details_image_text_panel.add(JLabel("Size KB"),cConstraints)
        cConstraints.gridx = 1
	cConstraints.gridy = 5
        details_image_text_panel.add(JLabel(str(image_selected.get_size_KB_image())),cConstraints)
        
class ModifyImageButtonListener (ActionListener):
    """
    Help to define the actions after an action is executed
    """
    def __init__(self, jlist,jpanel,list_images,jframe):

        ActionListener.__init__(self)
        self._spacer_panels = Dimension(5, 5)
        self.jlist = jlist
        self.jframe = jframe
        self.jpanel = jpanel
        self.list_images = []

    def updateList(self,list_images):
        """
        populate the Jlist with the list of images
        """
        self.list_images = list_images
        
    def actionPerformed(self, event):
        """
        after an image is selected the sout pane is enabled and display  the image information
        """
        selections = self.jlist.getSelectedIndex()
        image_selected = ImageFile()
        image_selected = self.list_images[selections]
        modify_image_panel = ModifyImage(image_selected,self.jframe)


