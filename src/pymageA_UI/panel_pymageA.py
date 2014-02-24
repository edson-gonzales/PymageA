from javax.swing import JPanel
from javax.swing import JButton
from javax.swing import JLabel
from javax.swing import JOptionPane
from javax.swing import JList
from javax.swing import JScrollPane
from javax.swing import BoxLayout
from javax.swing import Box
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder
from java.awt import BorderLayout
from java.awt import FlowLayout
from java.awt import Dimension
from java.awt import GridBagLayout
from java.awt import GridBagConstraints
from java.awt import Color
from javax.swing import JFileChooser
from java.awt.event import MouseAdapter
from modules.list_images_module.list_images import ListImages
from modules.image_modules.imageFile import ImageFile
from list_model import GeneratedListModel
from list_model import ImageRenderer
from pymageA_mouse_listener import JListMouseListener
from pymageA_mouse_listener import ModifyImageButtonListener
from javax.swing import DefaultListModel

class Panel_pymageA(JPanel):
    _spacer_components = Dimension(2, 2)
    _spacer_panels = Dimension(5, 5)
    def __init__(self,jframe):
        JPanel.__init__(self)
        self.jframe = jframe
        self.list_image = JList()
        self.details_image_panel =  JPanel()
        self.list_images_found = []
        self.setLayout(BoxLayout(self, BoxLayout.Y_AXIS))
        self.add(Box.createRigidArea(self._spacer_panels))
        self.listener_mouse =  JListMouseListener(self.list_image,self.details_image_panel,self.list_images_found)
        self.listener_mouse_button_modify =  ModifyImageButtonListener(self.list_image,self.details_image_panel,self.list_images_found,self.jframe)
        self.north_panel() #direcotry and buttons panel to search images
        self.center_panel() #image panel
        self.south_panel() #details_panel



    def north_panel(self):
        north_panel = JPanel()
        north_panel.setLayout(BoxLayout(north_panel, BoxLayout.Y_AXIS))
        north_panel.add(Box.createRigidArea(self._spacer_panels))
        path_panel = JPanel()
        layout_path = FlowLayout()
        path_panel.setLayout(layout_path)
        layout_path.setAlignment(FlowLayout.LEFT)
        path_panel.add(JButton("Search..",actionPerformed = self.search_button_clicked))
        self._path = JLabel("")
        path_panel.add(self._path)
        buttons_panel= JPanel()
        buttons_panel.setLayout(BoxLayout(buttons_panel, BoxLayout.X_AXIS))
        buttons_panel.add(Box.createRigidArea(self._spacer_components))
        buttons_panel.add(JButton("All Images",actionPerformed = self.option_all_image_button_clicked))
        buttons_panel.add(JButton("Duplicates Images by Size"))
        buttons_panel.add(JButton("Duplicates Images by Name", actionPerformed = self.option_duplicates_by_name_image_button_clicked))
        north_panel.add(path_panel,BorderLayout.NORTH)
        north_panel.add(buttons_panel,BorderLayout.SOUTH)
        self.add(north_panel,BorderLayout.NORTH)

    def option_all_image_button_clicked(self,event):
        if self._path.getText()!='':

            listImage = ListImages()
            list_of_directories = listImage.get_all_nested_directories(self._path.getText())
            size_of_list_of_folders = len(list_of_directories)
            lista= []
            self.list_images_found = listImage.get_all_images_from_directory \
								(size_of_list_of_folders, lista, list_of_directories)
            
            self.listener_mouse.updateList(self.list_images_found)
            self.listener_mouse_button_modify.updateList(self.list_images_found)
            for pos in range(len(self.list_images_found)):
                #self.list_image_model.addImage(self.list_images_found [pos].get_full_path_with_name_image_type())
                #self.list_image_model.update()
                self.list_image_model.addElement(str(self.list_images_found [pos]))
                

    def option_duplicates_by_name_image_button_clicked(self,event):
        if self._path.getText()!='':
            listImage = ListImages()
            list_of_firectories = listImages.get_all_nested_directories(self.test_path.getText())
            size_of_list_of_folders = len(list_of_directories)
            search_type = SearchDuplicatesByName()
            self.list_image_found = listImage.SearchDuplicatesByName()
            list_of_images_to_look_for = listImage.search_images_in_path \
									(self._path.getText(), search_type, size_of_list_of_folders, \
									list_of_images, list_of_directories)
		

            
    def search_button_clicked(self,event):
        chooser = JFileChooser()
        current_directory = chooser.getCurrentDirectory()
        chooser.setCurrentDirectory(current_directory)
        chooser.setDialogTitle("Open Folder")
        chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
        returnVal = chooser.showOpenDialog(chooser)
        if returnVal == JFileChooser.APPROVE_OPTION:
            currentDirectory = chooser.getSelectedFile()
            self._path.setText(currentDirectory.getAbsolutePath())
            print "soy "+self._path.getText()

    def center_panel(self):
        center_panel = JPanel()
      
        self.list_image_model = DefaultListModel()#GeneratedListModel()
        #self.list_image.setCellRenderer(ImageRenderer())
        self.list_image.setModel(self.list_image_model)
        self.list_image.setVisibleRowCount(22)
        self.list_image.addListSelectionListener(self.listener_mouse)
        scroll_pane =  JScrollPane(self.list_image)
        center_panel.add(scroll_pane)
        self.add(center_panel,BorderLayout.CENTER)

    def south_panel(self):
        south_panel =  JPanel()
        south_panel.setLayout(BoxLayout(south_panel, BoxLayout.X_AXIS))
        south_panel.add(Box.createRigidArea(self._spacer_panels))
        self.details_image(south_panel)
        self.add(south_panel,BorderLayout.SOUTH)

    def details_image(self,south_panel):
        #self.details_image_panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED), "Details Image"))
        self.details_image_panel.setLayout(BoxLayout(self.details_image_panel, BoxLayout.X_AXIS))
        self.details_image_panel.add(Box.createRigidArea(self._spacer_panels))
        south_panel.add(self.details_image_panel,BorderLayout.CENTER)
        
        button_modify = JButton("Modify")
        button_modify.addActionListener(self.listener_mouse_button_modify)
        south_panel.add(button_modify)
        #south_panel.add(JButton("Modify"))



