import unittest
import os
import sys
sys.path.append("../../../")

from main.modules.logger_module.logger import Logger

class ListloggerTest(unittest.TestCase):
	test_logger = ''
	path_resources = ''

	def setUp(self)	:
		file_path =''
		self.test_logger = Logger()
		self.path_resources = self.path_resources= os.path.dirname(os.path.abspath(__file__))+'/resources/'

	def test_log_file_exist_return_FALSE_if_file_does_not_exist(self):
		self.assertFalse(self.test_logger.log_file_exist(self.path_resources+'test/test.log'))
		
	def test_log_file_exist_return_TRUE_if_file_exists(self):
		self.assertTrue(self.test_logger.log_file_exist(self.path_resources+'test/test01.log'))
		
	def test_set_file_path_name_is_setting_the_correct_path_and_log_name(self):
		self.assertEquals(self.test_logger.get_file_path_name(),
							self.test_logger.get_file_path() + self.test_logger.get_file_name())	
		
	def test_get_file_path_log_is_getting_the_correct_path(self):
		self.assertEquals(self.test_logger.get_file_path(),self.test_logger.file_path)

	def test_get_file_name_is_getting_the_correct_name(self):
		self.assertEquals(self.test_logger.get_file_name(),self.test_logger.name_log)
		
	def test_get_file_path_name_is_getting_the_correct_path_and_log_name(self):
		self.assertEquals(self.test_logger.get_file_path_name(),self.test_logger.file_path_name)

	def test_set_info_is_registering_in_log(self):
		self.test_logger.set_info("This only a information")
		self.assertTrue(self.test_logger.search_text_in_log_file('This only a information'))	

	def test_set_warning_is_registering_in_log(self):
		self.test_logger.set_warning("This only a warning message")
		self.assertTrue(self.test_logger.search_text_in_log_file('This only a warning message'))
			
	def test_set_error_is_registering_in_log(self):
		self.test_logger.set_error("This a error message 0001")
		self.assertTrue(self.test_logger.search_text_in_log_file('This a error message 0001'))
	
	def test_if_set_is_not_executed_then_message_messsage_is_not_registered_in_log(self):
		self.assertFalse(self.test_logger.search_text_in_log_file('Other message error message 0002'))

	def test_if_two_logger_objects_are_bound_to_the_same_object(self):
		self.test_other_logger = Logger()
		self.assertTrue(self.test_logger is self.test_other_logger)

if __name__ == "__main__":
	unittest.main()	
	