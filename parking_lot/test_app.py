"""
Build a test suite and execute all the test cases
"""
import unittest

suite = unittest.TestSuite()
testmodules = [
    'tests.test_car',
    'tests.test_parking_lot',
    'tests.test_processor',
    'tests.test_search_parking'
]

for t in testmodules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
