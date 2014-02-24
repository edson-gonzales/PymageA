from javax.swing import JOptionPane
from javax.swing import JPanel
from javax.swing import JLabel
from javax.swing import JComboBox
from javax.swing import JButton

from javax.swing import JRadioButton
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
    _spacer_components = Dimension(2, 2)
    _spacer_panels = Dimension(5, 5)
    def __init__(self, image_details, jframe):
        self.jframe = jframe
        self.frame_details = JFrame("Modify Image")
        self.image_details = image_details
        self.height_pixels = JComboBox()
        self.width_pixels = JComboBox()
        self.angle_image = JComboBox()
        self.radio_resize = JRadioButton("Resize Image")
        self.radio_resize.setSelected(True)
        self.radio_rotate =JRadioButton("Rotate Image")
        self.group_radio = ButtonGroup()
        main_panel_modify =  self.frame_details.getContentPane()
        layout = BorderLayout()
        main_panel_modify.setLayout(layout)
        self.frame_details.setSize(Dimension(500,350))
        self.jframe.setEnabled(False)
        self.frame_details.setVisible(True)
        self.center_panel_options()
        
        self.south_panel_options()
        

    def center_panel_options(self):
        center_panel = JPanel()
        
        center_panel.setLayout(BoxLayout(center_panel, BoxLayout.Y_AXIS))
        center_panel.add(Box.createRigidArea(self._spacer_components))
        #JPanel Resize image
        
        self.resize_option(center_panel)
        self.group_radio.add(self.radio_resize)
        self.rotate_option(center_panel)
        self.group_radio.add(self.radio_rotate)
        self.frame_details.getContentPane().add(center_panel,BorderLayout.CENTER)

    def south_panel_options(self):
        south_panel = JPanel()
        south_panel.setLayout(BoxLayout(south_panel, BoxLayout.X_AXIS))
        south_panel.add(Box.createRigidArea(self._spacer_components))
        south_panel.add(JButton("OK",actionPerformed =  self.ok_button_clicked))
        south_panel.add(JButton("Cancel", actionPerformed =  self.cancel_button_clicked))
        self.update_values()
        self.frame_details.getContentPane().add(south_panel,BorderLayout.SOUTH)

    def resize_option(self, center_panel):
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

    def ok_button_clicked(self,event):
        if self.radio_resize.isSelected():
            print "mi group"
            if (self.height_pixels.getSelectedItem() == str(self.image_details.get_file_size_high()) and self.width_pixels.getSelectedItem() == str(self.image_details.get_file_size_width()) ):
                JOptionPane.showMessageDialog(None,"Enter new values to resize the image","Message image",JOptionPane.PLAIN_MESSAGE );
            else: #save the changes
                self.image_details.resize_image(int(self.height_pixels.getSelectedItem()), int(self.width_pixels.getSelectedItem()))
                
        if self.radio_rotate.isSelected():
            self.image_details.rotate_image(int(self.angle_image.getSelectedItem()))
        self.jframe.setEnabled(True)
        self.frame_details.dispose()
        
    def cancel_button_clicked(self, event):
        self.jframe.setEnabled(True)
        self.frame_details.dispose()

    def update_values(self):
        #print "siy ahwig and wirfu,",self.image_details.get_file_size_high(), "eeeww",self.image_details.get_file_size_width()
        self.height_pixels.setSelectedItem(str(self.image_details.get_file_size_high()))
        self.width_pixels.setSelectedItem(str(self.image_details.get_file_size_width()))
        