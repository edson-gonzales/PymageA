import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='C:\Users\mauricio\Desktop\Phyton\ejer\logger1/myapp.log',
                    filemode='a')
logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')