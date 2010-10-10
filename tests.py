import unittest

from refsrc import Referral

class TestReferral(unittest.TestCase):
    def test_main(self):
        testdata = [
            {'referrer' : 'http://www.google.com/search?num=30&hl=en&newwindow=1&biw=1136&bih=822&q=linux+boot+options&aq=6&aqi=g10&aql=&oq=linux+boo&gs_rfai=',
             }
            ]
        for ii, td in enumerate(testdata):
            ref = Referral(td['referrer'])
            self.assertEqual(td['referrer'], ref.referrer)
