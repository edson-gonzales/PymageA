from coverage import coverage
cov = coverage()
cov.start()

import unittest

from test_list_images.test_list_images import TestListImages
#from test_image.image_file_test import TestImageFile
#from logger_tests.logger_tests import ListloggerTest
#from test_search.test_search_by_size import TestSearchBySize
#from test_search.test_search_by_name import TestSearchByName
#from test_search.test_search_by_rms import TestSearchByRMS

suite = unittest.TestSuite()

suite.addTests(unittest.makeSuite(TestListImages))
#suite.addTests(unittest.makeSuite(TestImageFile))
#suite.addTests(unittest.makeSuite(ListloggerTest))
#suite.addTests(unittest.makeSuite(TestSearchByName))
#suite.addTests(unittest.makeSuite(TestSearchBySize))
#suite.addTests(unittest.makeSuite(TestSearchByRMS))

unittest.TextTestRunner(verbosity = 2).run(suite)
cov.stop()
cov.html_report(directory='report')