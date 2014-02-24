from javax.swing import JLabel
from java.awt import Graphics
from java.awt import Image
from  java.awt import Component
from javax.swing import ImageIcon
from modules.image_modules.manager_image import ManagerImage

class ScaledImageLabel(JLabel):
    def __init__(self):
        JLabel.__init__(self)

    def paintComponent(self,g):
        #icon = ImageIcon()
        icon = self.getIcon();
        if (icon != None):
            ManagerImage.drawScaledImage(icon.getImage(),self, g)# To change this template, choose Tools | Templates


