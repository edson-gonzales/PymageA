import logging

class mylogger:
	""" an instance register the message,error or warning in the log
	"""

	filename=""
	level=0

	def __init__(self,filenamelog,levellog):
		logging.basicConfig(level=logging.DEBUG,
							format='%(asctime)s %(levelname)-8s %(message)s',
							datefmt='%a, %d %b %Y %H:%M:%S',
							filename=filenamelog,
							filemode='a')
		filename=filenamelog

		
	def set_info(self,message):
		logging.info(message)
			
	def set_warning(self,warning):
		logging.warning	(warning)

	def set_error(self,myerror):
		logging.error(myerror)
	