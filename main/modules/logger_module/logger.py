import os
import logging
import sys
import time
from singlenton import Singleton



class Logger():
    """
    Logger object.
    
    """
    __metaclass__ = Singleton

    
    file_path = ''
    name_log = ''
    file_path_name = ''
    

    def __init__(self):
        self.name_log = self.set_file_name()
        self.file_path = self.set_file_path()
        self.file_path_name = self.set_file_path_name()
        self. set_config(self.file_path_name)



    def set_config(self, file_path_name):
        level = logging.DEBUG
        format = '%(asctime)s %(levelname)-8s %(message)s' 
        datefmt = '%a, %d %b %Y %H:%M:%S'
        filemode = 'a'
    
        """ Configure how the content of the file will be registered
        """
        logging.basicConfig(level = level,
                            format = format,
                            datefmt = datefmt,
                            filename = file_path_name,
                            filemode = filemode)
    
    """ Begin the methods related to set and get for attibutes: path, log name 
        and path complete(file_path_name= path + log name)
    """
    def set_file_path (self):
        actual_path = os.getcwd()
        for  i in '123':
            file_base_name, file_extension = os.path.split(actual_path)
            actual_path = file_base_name
        file_path = actual_path +'\\'+'logs'+'\\'
        return file_path 
        
    def get_file_path (self):
        return self.file_path

    def set_file_name(self):
        name = 'LogImage'
        name_log_date = time.strftime("%Y%m%d")
        name_log = name + name_log_date + '.log'
        return name_log

    def get_file_name(self):
        return self.name_log     

    def set_file_path_name(self):
        file_path_name = self.get_file_path() + self.get_file_name()
        return file_path_name     

    def get_file_path_name(self):
        return self.file_path_name
        

    """ END the methods relatd to set and get for attibutes
    """

    def log_file_exist(self, file_path_name):
        return os.path.isfile(file_path_name)     #file exist 
    """
    The below funtcions registered the messages in the log according to their type: error, info or warning
    """

    def set_info(self, message):
        if self.log_file_exist(self.file_path_name):
            logging.info(message)
        else:
            print "The log "+ self.name_log + "does not exist in the directory"     
            
    def set_warning(self, warning):
        if self.log_file_exist(self.file_path_name):
            logging.warning (warning)
        else:
            print "The log "+ self.name_log + "does not exist in the directory"     

    def set_error(self, error):
        if self.log_file_exist(self.file_path_name):
            logging.error(error)
        else:
            print "The log "+ self.name_log + "does not exist in the directory"     
        
    """
    search_text_in_log_file, help to verify is the message(info,error and warning) was registered in the log

    """
    
    def search_text_in_log_file(self, text) :
        try:
            with open(self.file_path_name, 'r') as searchfile:
                for line in searchfile:
                    if text in line:
                        return True  
            return False 
        except:           
            print 'The log : ' + self.file_path_name + 'cannot be opened'
