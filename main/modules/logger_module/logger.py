import os
import logging
import sys
import time
from singlenton import Singleton

class Logger():
    """
    Class Logger  help to registered messages,warning and errors in a log file.
    
    """
    __metaclass__ = Singleton

    file_path = ''     # only path for example  C:\Users
    name_log = ''       
    file_path_name = ''    #combination of path and log name
    
    def __init__(self):
        self.set_file_name()
        self.set_file_path()
        self.set_file_path_name()
        self.set_config(self.get_file_path_name())

    def set_config(self, file_path_name):
        """ Configure how the content of the file log will be registered.
            Keyword arguments:
            level: Set the root logger level to the specified level.
            format: Use the specified format string in this case: datetime,level,message. 
            datefmt : Use the specified date/time format
            file_path_name: file path name were the log will be saved.
            filemode:Specifies the mode to open the file.

        """
        level = logging.DEBUG
        format = '%(asctime)s %(levelname)-8s %(message)s' 
        datefmt = '%a, %d %b %Y %H:%M:%S'
        filemode = 'a'
    

        logging.basicConfig(level = level,
                            format = format,
                            datefmt = datefmt,
                            filename = file_path_name,
                            filemode = filemode)
    
    """ Begin the methods related to set and get for attibutes: path, log name 
        and path complete(file_path_name= path + log name)
    """
    def set_file_path (self):
        """ assing the log path (for example C:\Users\logs\) to the variable
        Keyword arguments:
        actual_path: this obtains the path until this file(logger.py)
        file_base_name: is the result of the split the actual_path, to help obtains 
        the log path 

        """
        actual_path = os.path.dirname(os.path.abspath(__file__))
        for  i in range(1,4):
            file_base_name, file_extension = os.path.split(actual_path)
            actual_path = file_base_name
        self.file_path = actual_path +'\\'+'logs'+'\\'
        
    def get_file_path (self):
        return self.file_path

    def set_file_name(self):
        """ Help to obtain the name log.
        name: define the string part of the log name: LogImage
        name_log_date : define the date part of the log name: 20140211
        the result is the combination of both:LogImage20140211
        """
        name = 'LogImage'
        name_log_date = time.strftime("%Y%m%d")
        self.name_log = name + name_log_date + '.log'

    def get_file_name(self):
        return self.name_log     

    def set_file_path_name(self):
        """ file_path_name is the combination of log path and log name
        """
        self.file_path_name = self.get_file_path() + self.get_file_name()

    def get_file_path_name(self):
        return self.file_path_name
        
    """ END the methods relatd to set and get for attibutes
    """

    def log_file_exist(self, file_path_name):
        """
        this method help to know if the file exist in the path(file_path)
        """
        return os.path.isfile(file_path_name)      
    
    """
    The below funtcions registered the messages in the log according to their type: error, info or warning
    """

    def set_info(self, message):
        """ this method registered the info messages in the log, previous verfication if the file log exist.
        """
        if self.log_file_exist(self.file_path_name):
            logging.info(message)
        else:
            print "The log "+ self.name_log + "does not exist in the directory"     
            
    def set_warning(self, warning):
        """ this method registered the warning messages in the log, previous verfication if the file log exist.
        """
        if self.log_file_exist(self.file_path_name):
            logging.warning (warning)
        else:
            print "The log "+ self.name_log + "does not exist in the directory"     

    def set_error(self, error):
        """ this method registered the error messages in the log, previous verfication if the file log exist.
        """
        if self.log_file_exist(self.file_path_name):
            logging.error(error)
        else:
            print "The log "+ self.name_log + "does not exist in the directory"     
          
    def search_text_in_log_file(self, text) :
        """
        search_text_in_log_file, help to verify is the message(info,error and warning) was registered in the log

        """
        try:
            with open(self.file_path_name, 'r') as searchfile:
                for line in searchfile:
                    if text in line:
                        return True  
            return False 
        except:           
            print 'The log : ' + self.file_path_name + 'cannot be opened'
