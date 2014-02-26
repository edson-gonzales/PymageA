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
from javax.swing import ListSelectionModel
from java.awt import FlowLayout
from java.awt import Dimension
from javax.swing import ImageIcon
from java.awt import GridBagLayout
from java.awt import Font
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
from modules.searcher_module.search_by_name import SearchDuplicatesByName
from modules.searcher_module.search_by_size import SearchDuplicatesBySize
from javax.swing import JPanel
from javax.swing import JOptionPane


class Panel_pymageA(JPanel):
    _spacer_components = Dimension(2, 2)
    _spacer_panels = Dimension(5, 5)
    def __init__(self,jframe):
        JPanel.__init__(self)
        self.jframe = jframe
        self.list_image_model = DefaultListModel()
        self.list_image = JList(self.list_image_model )
        self.list_image.setSelectionMode(ListSelectionModel.SINGLE_SELECTION )
        self.details_image_panel =  JPanel()
        self.south_panel = JPanel()
        self.list_images_found = []


        self._path = JLabel("")
        #self.button_modify = JButton("Modify image")
        self.button_modify = JButton(ImageIcon("icons/modify.png"))
        self.button_modify.setToolTipText("Click this button to modify the image.")
        self.setLayout(BoxLayout(self, BoxLayout.Y_AXIS))
        self.add(Box.createRigidArea(self._spacer_panels))
        self.listener_mouse =  JListMouseListener(self.list_image,self.details_image_panel,self.list_images_found,self.button_modify,self.south_panel)
        self.listener_mouse_button_modify =  ModifyImageButtonListener(self.list_image,self.details_image_panel,self.list_images_found,self.jframe)
        self.north_panel() #direcotry and buttons panel to search images
        self.center_panel() #image panel
        self.south_panel_p() #details_panel



    def north_panel(self):
        north_panel = JPanel()
        north_panel.setLayout(BoxLayout(north_panel, BoxLayout.Y_AXIS))
        north_panel.add(Box.createRigidArea(self._spacer_panels))
        path_panel = JPanel()
        layout_path = FlowLayout()
        path_panel.setLayout(layout_path)
        layout_path.setAlignment(FlowLayout.LEFT)
        #self.button_modify = JButton(ImageIcon("icons/modify.png"))
        #self.button_modify.setToolTipText("Click this button to modify the image.")
        open_folder_button = JButton("Open Folder..",ImageIcon("icons/folderOpen.png"),actionPerformed = self.search_button_clicked)
        open_folder_button.setFont(Font("sansserif",Font.BOLD,9))
        
        open_folder_button.setToolTipText("Click this button select folder to search images.")
        #path_panel.add(JButton("Open Folder..",ImageIcon("icons/modify.png"),actionPerformed = self.search_button_clicked))
        path_panel.add(open_folder_button)
        path_panel.add(self._path)
        buttons_panel= JPanel()
        buttons_panel.setLayout(BoxLayout(buttons_panel, BoxLayout.X_AXIS))
        buttons_panel.add(Box.createRigidArea(self._spacer_components))
        all_images_button = JButton("All Images",ImageIcon("icons/searchAll.png"),actionPerformed = self.option_all_image_button_clicked)
        all_images_button.setFont(Font("sansserif",Font.BOLD,9))
        all_images_button.setPreferredSize(Dimension(40, 40))
        all_images_button.setToolTipText("Click this button to search all images with extension jpg, png and bmp.")
        #buttons_panel.add(JButton("All Images",actionPerformed = self.option_all_image_button_clicked))
        buttons_panel.add(all_images_button)

        duplicates_images_button = JButton("Duplicates Images by Size",ImageIcon("icons/searchImages.png"),actionPerformed = self.option_duplicates_by_size_image_button_clicked)
        duplicates_images_button.setFont(Font("sansserif",Font.BOLD,9))
        duplicates_images_button.setPreferredSize(Dimension(40, 40))
        duplicates_images_button.setToolTipText("Click this button to search all duplicate images by size with format: jpg, png and bmp.")

        #buttons_panel.add(JButton("Duplicates Images by Size",actionPerformed = self.option_duplicates_by_size_image_button_clicked))
        buttons_panel.add(duplicates_images_button)

        duplicates_images_name_button = JButton("Duplicates Images by Size",ImageIcon("icons/searchIName.png"),actionPerformed = self.option_duplicates_by_name_image_button_clicked)
        duplicates_images_name_button.setFont(Font("sansserif",Font.BOLD,9))
        duplicates_images_name_button.setPreferredSize(Dimension(40, 40))
        duplicates_images_name_button.setToolTipText("Click this button to search all duplicate images by Name with format: jpg, png and bmp.")

        
        buttons_panel.add(duplicates_images_name_button)

        duplicates_images_root_button = JButton("Duplicates Images using the root mean squared",ImageIcon("icons/searchIRoot.png"),actionPerformed = self.option_duplicates_usign_root_mean_square_button_clicked)
        duplicates_images_root_button.setFont(Font("sansserif",Font.BOLD,9))
        duplicates_images_root_button.setPreferredSize(Dimension(40, 40))
        duplicates_images_root_button.setToolTipText("Click this button to search all duplicate images using method root mean squared to format: jpg, png and bmp.")

        
        buttons_panel.add(duplicates_images_root_button)
        north_panel.add(path_panel,BorderLayout.NORTH)
        north_panel.add(buttons_panel,BorderLayout.SOUTH)
        self.add(north_panel,BorderLayout.NORTH)

    def option_all_image_button_clicked(self, event):
        """ When user perform a click in "All Images" button then all images that have
        jpg, bmp, png extension are displayed in Jlist """
        if self._path.getText()!='':
           if(self.list_image_model.getSize()!= 0):
               self.list_image.model.removeAllElements()
           listImage = ListImages()
           list_of_directories = listImage.get_all_nested_directories(self._path.getText())
           print "despues de lo directorios"
           size_of_list_of_folders = len(list_of_directories)
           print "despues del tamnanio"
           lista= []
           self.list_images_found = listImage.get_all_images_from_directory \
								(size_of_list_of_folders, lista, list_of_directories)
            
           self.listener_mouse.updateList(self.list_images_found)
           
           self.listener_mouse_button_modify.updateList(self.list_images_found)
           
           for pos in range(len(self.list_images_found)):
                #self.list_image_model.addImage(self.list_images_found [pos].get_full_path_with_name_image_type())
                #self.list_image_model.update()
                self.list_image_model.addElement(str(self.list_images_found [pos]))
        else:
            JOptionPane.showMessageDialog(None,"Select a path to start the search for image files","Incorect Path", JOptionPane.ERROR_MESSAGE )
                

    def option_duplicates_by_size_image_button_clicked(self, event):
        if self._path.getText()!='':
            if(self.list_image_model.getSize() != 0):
                self.list_image_model.removeAllElements()
            listImage = ListImages()
            self.list_image_model.clear()
            list_of_images = []
            list_of_directories = listImage.get_all_nested_directories(self._path.getText())
            size_of_list_of_folders = len(list_of_directories)
            search_type = SearchDuplicatesBySize()
            #self.list_image_found = listImage.SearchDuplicatesByName()
            self.list_images_found = listImage.search_images_in_path \
									(self._path.getText(), search_type, size_of_list_of_folders, \
									list_of_images, list_of_directories)

            self.listener_mouse.updateList(self.list_images_found)
            self.listener_mouse_button_modify.updateList(self.list_images_found)
            for pos in range(len(self.list_images_found)):
               self.list_image_model.addElement(str(self.list_images_found [pos]))
        else:
            JOptionPane.showMessageDialog(None,"Select a path to start the search for image files","Incorect Path", JOptionPane.ERROR_MESSAGE )


    def option_duplicates_by_name_image_button_clicked(self,event):
        """ When user perform a click in "Duplicates Images by Name" button then all images that have
        jpg, bmp, png extension are displayed in Jlist """

        if self._path.getText()!='':
            if(self.list_image_model.getSize() != 0):
                self.list_image_model.removeAllElements()
            listImage = ListImages()
            self.list_image_model.clear()
            list_of_images = []
            list_of_directories = listImage.get_all_nested_directories(self._path.getText())
            size_of_list_of_folders = len(list_of_directories)
            search_type = SearchDuplicatesByName()
            #self.list_image_found = listImage.SearchDuplicatesByName()
            self.list_images_found = listImage.search_images_in_path \
									(self._path.getText(), search_type, size_of_list_of_folders, \
									list_of_images, list_of_directories)

            self.listener_mouse.updateList(self.list_images_found)
            self.listener_mouse_button_modify.updateList(self.list_images_found)
            for pos in range(len(self.list_images_found)):
               self.list_image_model.addElement(str(self.list_images_found [pos]))
        else:
            JOptionPane.showMessageDialog(None,"Select a path to start the search for image files","Incorect Path", JOptionPane.ERROR_MESSAGE )
                
    def option_duplicates_usign_root_mean_square_button_clicked(self, event):
        if self._path.getText()!='':
            pass
        else:
            JOptionPane.showMessageDialog(None,"Select a path to start the search for image files","Incorect Path", JOptionPane.ERROR_MESSAGE )
            
    def search_button_clicked(self,event):
        """
        FileChooser is displayed to select a directory
        """
        chooser = JFileChooser()
        current_directory = chooser.getCurrentDirectory()
        chooser.setCurrentDirectory(current_directory)
        chooser.setDialogTitle("Open Folder")
        chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
        returnVal = chooser.showOpenDialog(chooser)
        if returnVal == JFileChooser.APPROVE_OPTION:
            currentDirectory = chooser.getSelectedFile()
            self._path.setText(currentDirectory.getAbsolutePath())
            

    def center_panel(self):
        """
        Panel where Jlist is content
        """
        center_panel = JPanel()
      
        self.list_image_model = DefaultListModel()#GeneratedListModel()
        #self.list_image.setCellRenderer(ImageRenderer())
        self.list_image.setModel(self.list_image_model)
        self.list_image.setVisibleRowCount(22)
        self.list_image.addListSelectionListener(self.listener_mouse)
        scroll_pane =  JScrollPane(self.list_image)
        center_panel.add(scroll_pane)
        self.add(center_panel,BorderLayout.CENTER)

    def south_panel_p(self):
        """
        JPanel where details about image selected in Jlist are displayed
        """
        self.south_panel.setLayout(BoxLayout(self.south_panel, BoxLayout.X_AXIS))
        self.south_panel.add(Box.createRigidArea(self._spacer_panels))
        self.details_image()
        self.add(self.south_panel,BorderLayout.SOUTH)
        #self.south_panel.setVisible(False)
        #self.details_image.setVisible(false)

    def details_image(self):
        #self.details_image_panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED), "Details Image"))
        self.details_image_panel.setLayout(BoxLayout(self.details_image_panel, BoxLayout.X_AXIS))
        self.details_image_panel.add(Box.createRigidArea(self._spacer_panels))
        self.south_panel.add(self.details_image_panel,BorderLayout.CENTER)
        self.button_modify.addActionListener(self.listener_mouse_button_modify)
        self.button_modify.setEnabled(False)
        self.south_panel.add(self.button_modify)
    
     


