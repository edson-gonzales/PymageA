from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JButton
from java.awt import BorderLayout
from java.awt import FlowLayout
from java.awt import Toolkit
from java.awt import Dimension
from pymageA_UI.panel_pymageA import Panel_pymageA

class MainWindow():
    """
    The MainWindows class handles the windows(frames and panels) were the UI will be displayed
    """
    def initilialize_ui(self):
        self.initilialize_frame()
        self.create_center_panel()
        
    def initilialize_frame(self):
        """
        This function helps to define the Frame and its characteristics of the frame like: title,borders, height and size

        Keyword arguments:

        frame  --  it is an instance of JFrame, it helps to put the title
        main_panel --
        layout -- help to put the border to main_panel
        screen_Size -- obtains the total of screen size and the value obtained helps
                       to define the size for the frame (frame.setSize)


        """
        self.frame = JFrame("PymageA",defaultCloseOperation= JFrame.EXIT_ON_CLOSE)
        main_panel =  self.frame.getContentPane()
        layout = BorderLayout()
        screenSize = Toolkit.getDefaultToolkit().getScreenSize()
        self.frame.setSize(Dimension(int(screenSize.getWidth()/1.5), int(screenSize.getHeight()/1.5)))
        main_panel.setLayout(layout)


    def show_window(self):
        """
        This function help to the window can be visible.
        """
        self.frame.setVisible(True)

    def create_center_panel(self):
        """
        Creates the central Pane.
        Keyword arguments:
        central_panel: it is a instance of Panel_pymageA

        """
        center_panel = Panel_pymageA(self.frame)
        self.frame.getContentPane().add(center_panel, BorderLayout.CENTER)




if __name__ == "__main__":
    window = MainWindow()
    window.initilialize_ui()
    window.show_window()



