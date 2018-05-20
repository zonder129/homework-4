# -*- coding: utf-8 -*-

import sys
import unittest

from tests.AddImageTests import AddImageTests
from tests.CreateAlbumTests import CreateAlbumTests

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreateAlbumTests),
        unittest.makeSuite(AddImageTests),
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())
