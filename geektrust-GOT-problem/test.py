"""
Build a test suite and execute all the test cases
"""
import unittest

suite = unittest.TestSuite()
testmodules = [
    'tests.test_kingdom',
    'tests.test_message',
    'tests.test_prblm1_processor',
    'tests.test_voting_machine',
    'tests.test_prblm2_processor',
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
