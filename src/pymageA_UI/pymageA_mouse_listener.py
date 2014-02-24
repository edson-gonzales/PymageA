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
from javax.swing import ImageIcon
from image_pymageUI import ScaledImageLabel
from java.awt.event import ActionListener
from dialog_pymageA import Panel_modifyImage

class JListMouseListener(ListSelectionListener):
    
    def __init__(self, jlist,jpanel,list_images):
        self._spacer_panels = Dimension(5, 5)
        ListSelectionListener.__init__(self)
        self.jlist = jlist
        self.jpanel = jpanel
        self.list_images = []
        self.list_images = list_images
           
    def updateList(self,list_images):
        self.list_images = list_images
    def valueChanged(self,event):
        selections = self.jlist.getSelectedIndex()
        model = self.jlist.getModel()
        selec = model.getElementAt(selections)
        image_selected = ImageFile()
        image_selected = self.list_images[selections]
        element_image = self.jlist.getSelectedValues()
        self.jpanel.removeAll()
        self.jpanel.repaint()
        self.show_details_image(image_selected)
        self.jpanel.revalidate()
        
        

    def show_details_image(self,image_selected):
        details_image_text_panel = JPanel()
        details_image_text_panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED), "Details Image"))
        details_image_text_panel.setLayout(GridBagLayout())
        cConstraints = GridBagConstraints()
        cConstraints.weightx = 0.1
        cConstraints.weighty = 0.1
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 0
        details_image_text_panel.add(JLabel("Name"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 0
        details_image_text_panel.add(JLabel(image_selected.get_complete_image_with_type()),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 1
        details_image_text_panel.add(JLabel("Width:"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 1
        details_image_text_panel.add(JLabel(str(image_selected.get_file_size_width())),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 2
        details_image_text_panel.add(JLabel("Height"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 2
        details_image_text_panel.add(JLabel(str(image_selected.get_file_size_high())),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 3
        details_image_text_panel.add(JLabel("Size KB"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 3
        details_image_text_panel.add(JLabel(str(image_selected.get_size_KB_image())),cConstraints)
        self.jpanel.add(details_image_text_panel)

        #create secondt jpanel to show image
        image_panel = JPanel()
        image_panel.setLayout(BoxLayout( image_panel, BoxLayout.Y_AXIS))
        image_panel.add(Box.createRigidArea(self._spacer_panels))
        #labelImage = ScaledImageLabel()
        #image = ImageIO.read(File(image_selected.get_full_path_with_name_image_type()))
        #labelImage.setIcon(ImageIcon(image))
        labelImage = JLabel("mi image")
        image_panel.add(labelImage)
        self.jpanel.add(image_panel)
        
        #self.jbutton.setEnabled(True)# To change this template, choose Tools | Templates
class ModifyImageButtonListener (ActionListener):
    def __init__(self, jlist,jpanel,list_images,jframe):
        ActionListener.__init__(self)
        self._spacer_panels = Dimension(5, 5)
        self.jlist = jlist
        self.jframe = jframe
        self.jpanel = jpanel
        self.list_images = []
    def updateList(self,list_images):
        self.list_images = list_images
        
    def actionPerformed(self, event):
        selections = self.jlist.getSelectedIndex()
        image_selected = ImageFile()
        image_selected = self.list_images[selections]
        modify_image_panel = Panel_modifyImage(image_selected,self.jframe)
        print("click in buttonModify",image_selected.get_complete_image_with_type())

