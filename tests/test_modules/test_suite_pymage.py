from coverage import coverage
cov = coverage()
cov.start()

import unittest

from test_list_images.test_list_images import TestListImages
from test_image.image_file_test import TestImageFile

suite = unittest.TestSuite()

suite.addTests(unittest.makeSuite(TestListImages))
suite.addTests(unittest.makeSuite(TestImageFile))

unittest.TextTestRunner(verbosity = 2).run(suite)
cov.stop()
cov.html_report(directory='report')