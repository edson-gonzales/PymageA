from javax.swing import JOptionPane
from javax.swing import JPanel
from javax.swing import JLabel
from javax.swing import JComboBox
from javax.swing import JButton

from javax.swing import JRadioButton
from javax.swing import JCheckBox
from javax.swing import ButtonGroup
from javax.swing import JFrame
from java.awt import BorderLayout
from java.awt import FlowLayout
from java.awt import Dimension
from javax.swing import Box
from javax.swing import BorderFactory
from javax.swing import BoxLayout
from javax.swing.border import EtchedBorder
from java.awt import GridBagLayout
from java.awt import GridBagConstraints
from modules.image_modules.imageFile import ImageFile

class Panel_modifyImage:
    """
    class  where the options for rotate,resize and convert the images will be executed
    """
    _spacer_components = Dimension(2, 2)
    _spacer_panels = Dimension(5, 5)
    def __init__(self, image_details, jframe):
        """
        All values that will be used are declared in constructor
        """
        self.jframe = jframe
        self.frame_details = JFrame("Modify Image: " + image_details.get_complete_image_with_type())
        self.frame_details.setDefaultCloseOperation( self.frame_details.DO_NOTHING_ON_CLOSE )
        self.image_details = image_details
        self.height_pixels = JComboBox()
        self.width_pixels = JComboBox()
        self.angle_image = JComboBox()
        self.group_radio = ButtonGroup()
        self.radio_resize = JRadioButton("Resize Image")
        self.radio_resize.setSelected(True)
        self.radio_rotate =JRadioButton("Rotate Image")
        self.radio_convert =JRadioButton("Convert Image")
        main_panel_modify =  self.frame_details.getContentPane()
        layout = BorderLayout()
        main_panel_modify.setLayout(layout)
        self.frame_details.setSize(Dimension(500,350))
        self.jframe.setEnabled(False)
        self.frame_details.setVisible(True)
        self.center_panel_options()
        
        self.south_panel_options()
        

    def center_panel_options(self):
        """
        Show the options to modify the image
        """
        center_panel = JPanel()
        
        center_panel.setLayout(BoxLayout(center_panel, BoxLayout.Y_AXIS))
        center_panel.add(Box.createRigidArea(self._spacer_components))    
        self.resize_option(center_panel)
        self.group_radio.add(self.radio_resize)
        self.rotate_option(center_panel)
        self.group_radio.add(self.radio_rotate)
        self.convert_option(center_panel)
        self.group_radio.add(self.radio_convert)
        self.frame_details.getContentPane().add(center_panel,BorderLayout.CENTER)

    def south_panel_options(self):
        """
        Show the buttons Ok and Cancel
        """
        south_panel = JPanel()
        south_panel.setLayout(BoxLayout(south_panel, BoxLayout.X_AXIS))
        south_panel.add(Box.createRigidArea(self._spacer_components))
        south_panel.add(JButton("OK",actionPerformed =  self.ok_button_clicked))
        south_panel.add(JButton("Cancel", actionPerformed =  self.cancel_button_clicked))
        self.update_values()
        self.frame_details.getContentPane().add(south_panel,BorderLayout.SOUTH)

    def resize_option(self, center_panel):
        """
        Display the information required for resize an image in the JPanel
        """
        for number in range (9999):
            self.height_pixels.addItem(str(number+1))
            self.width_pixels.addItem(str(number+1))
        resize_panel = JPanel()       
        resize_panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED), "Resize Image"))
        resize_panel.setLayout(GridBagLayout())
        cConstraints = GridBagConstraints()
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridwidth = 2
        cConstraints.gridx = 0
	cConstraints.gridy = 0
        resize_panel.add(self.radio_resize)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 1
        resize_panel.add(JLabel("Width:"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 1
        resize_panel.add(self.width_pixels,cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 2
        resize_panel.add(JLabel("Heigh:"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 2
        resize_panel.add(self.height_pixels,cConstraints)
        center_panel.add(resize_panel)

    def rotate_option(self, center_panel):
        """
        Display the information required for rotate an image in the JPanel
        """
        for number in range (359):
            self.angle_image.addItem(str(number+1))
        rotate_panel = JPanel()
        rotate_panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED), "Rotate Image"))
        rotate_panel.setLayout(GridBagLayout())
        cConstraints = GridBagConstraints()
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridwidth = 2
        cConstraints.gridx = 0
	cConstraints.gridy = 0
        rotate_panel.add(self.radio_rotate)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 0
	cConstraints.gridy = 1
        rotate_panel.add(JLabel("Angle to Rotate:"),cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 1
        rotate_panel.add(self.angle_image,cConstraints)
        center_panel.add(rotate_panel)

    def convert_option(self,center_panel):
        """
         Display the information required for convert an image in the JPanel
        """
        self.group_formats = ButtonGroup()
        self.format_jpg = JRadioButton("jpg")
        self.format_jpg.setSelected(True)
        self.format_png = JRadioButton("png")
        self.format_bmp = JRadioButton("bmp")
        self.group_formats.add(self.format_jpg)
        self.group_formats.add(self.format_png)
        self.group_formats.add(self.format_bmp)
        convert_panel = JPanel()
        convert_panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(EtchedBorder.LOWERED), "Convert Image"))
        convert_panel.setLayout(GridBagLayout())
        cConstraints = GridBagConstraints()
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridwidth = 2
        cConstraints.gridx = 0
	cConstraints.gridy = 0
        convert_panel.add(self.radio_convert, cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 1
        convert_panel.add(self.format_jpg,cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 2
        convert_panel.add(self.format_png , cConstraints)
        cConstraints.fill = GridBagConstraints.NONE
        cConstraints.gridx = 1
	cConstraints.gridy = 3
        convert_panel.add(self.format_bmp,cConstraints)
        center_panel.add(convert_panel)


    def ok_button_clicked(self,event):
        """
        When OK button is clicked diferents actions are performed to validated the news values
        """
        exit = 1
        if self.radio_resize.isSelected():
            
            if (self.height_pixels.getSelectedItem() == str(self.image_details.get_file_size_high()) and self.width_pixels.getSelectedItem() == str(self.image_details.get_file_size_width()) ):
                JOptionPane.showMessageDialog(None,"Enter new values to resize the image","Message image",JOptionPane.PLAIN_MESSAGE );
                exit = -1
            else: #save the changes
                self.image_details.resize_image(int(self.height_pixels.getSelectedItem()), int(self.width_pixels.getSelectedItem()))
                
        if self.radio_rotate.isSelected():
            self.image_details.rotate_image(int(self.angle_image.getSelectedItem()))

        if self.radio_convert.isSelected():
            if self.format_jpg.isSelected():
                format_selected = self.format_jpg.getText()
            if self.format_png.isSelected():
                format_selected = self.format_png.getText()
            if self.format_bmp.isSelected():
                format_selected = self.format_bmp.getText()            
            if((self.image_details.get_file_type()).lower() == ("." + format_selected).lower()):
                JOptionPane.showMessageDialog(None, "The image cannot to convert to same format. Please select other format" ,"Convert Image",JOptionPane.PLAIN_MESSAGE );
                exit = -1
            else:
                self.image_details.convert_to_other_format(format_selected)

        if (exit ==1):
            self.jframe.setEnabled(True)
            self.frame_details.dispose()
        
    def cancel_button_clicked(self, event):
        """
        if not action is required in modify action, we can close the window with cancel button
        """
        self.jframe.setEnabled(True)
        self.frame_details.dispose()

    def update_values(self):
        """
        get the height and wifth an update the values of the image
        """
        self.height_pixels.setSelectedItem(str(self.image_details.get_file_size_high()))
        self.width_pixels.setSelectedItem(str(self.image_details.get_file_size_width()))
        