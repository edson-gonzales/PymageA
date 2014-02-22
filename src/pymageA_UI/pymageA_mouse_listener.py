
from java.awt import GridBagConstraints
from javax.swing import JLabel
from javax.swing import JList
from javax.swing import JPanel
from modules.image_modules.imageFile import ImageFile
from javax.swing.event import ListSelectionListener

class JListMouseListener(ListSelectionListener):

    def __init__(self, jlist,jpanel,list_images):
        self.jlist = jlist
        self.jpanel = jpanel
        self.list_images = []
        self.list_images = list_images
        ListSelectionListener.__init__(self)
        
    def get_image(self, path_name_image):
        print "path_name_iamge",path_name_image
        for i in range(len(self.list_images)):
            print "esesesfor ",self.list_images[i].get_file_size_width()," kkkkk",path_name_image,"---"
            if path_name_image == str(self.list_images[i]):
                return self.list_images[i]
        

    def valueChanged(self,event):
        element_image = ImageFile()
        
        selections = self.jlist.getSelectedIndex()
        #print"selecion ",selections
        path_name_image = self.jlist.getModel()
        element_image = self.get_image(path_name_image)
        #element_model= ImageFile(model.getElementAt(selections))
       # element_image = self.jlist.getSelectedValue()
        print "tet typer" ,type(element_image),":size",element_image.get_file_size_width() , "-- ";
        ##print "model" ,type(element_model), "-- ";


#        element_image = self.jlist.getSelectedValues()
        #print "kkk:",element_image.get_complete_image_with_type()

        #print"soy y empezare a poner a mi panel de images ",self.jlist.getSelectedValue()
        cConstraints = GridBagConstraints()
        cConstraints.weightx = 0.1
        cConstraints.weighty = 0.1
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 0
        self.jpanel.add(JLabel("Name"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 0
        self.jpanel.add(JLabel(""),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 1
        self.jpanel.add(JLabel("Width:"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 1
        self.jpanel.add(JLabel(""),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 2
        self.jpanel.add(JLabel("Height"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 2
        self.jpanel.add(JLabel(""),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 3
        self.jpanel.add(JLabel("Size KB"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 3
        self.jpanel.add(JLabel(""),cConstraints)
        self.jpanel.revalidate()
        #self.jbutton.setEnabled(True)# To change this template, choose Tools | Templates
