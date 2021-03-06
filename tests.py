# -*- coding: utf-8 -*-
import unittest
import os

from pyreferrer import Referrer

class TestReferrer(unittest.TestCase):
    def test_searchengines(self):
        testdata = [
            {'referrer' : 'http://www.google.com/search?num=30&hl=en&newwindow=1&biw=1136&bih=822&q=linux+boot+options&aq=6&aqi=g10&aql=&oq=linux+boo&gs_rfai=',
             'searchengine' : 'google',
             'searchphrase' : 'linux boot options',
             'is_search' : True,
             },
            {'referrer' : 'http://www.google.de/search?q=tex+math+to+image&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:de:official&client=firefox-a',
             'searchengine' : 'google',
             'searchphrase' : 'tex math to image',
             'is_search' : True,
             },
            {'referrer' : 'http://www.google.co.in/search?q=+++++++Language+Outside+Chomsky+Hierarchy',
             'searchengine' : 'google',
             'searchphrase' : 'Language Outside Chomsky Hierarchy',
             'is_search' : True,
             },
            {'referrer' : 'http://www.bing.com/search?q=automated+quality+assurance&qs=n&sk=&adlt=strict&first=31&FORM=PERE2',
             'searchengine' : 'bing',
             'searchphrase' : 'automated quality assurance',
             'is_search' : True,
             },
            {'referrer' : 'http://search.yahoo.co.jp/search?p=kernel+boot+parameter+linux&search.x=1&fr=top_ga1_sa&tid=top_ga1_sa&ei=UTF-8&aq=&oq=',
             'searchengine' : 'yahoo',
             'searchphrase' : 'kernel boot parameter linux',
             'is_search' : True,
             },
            {'referrer' : 'http://us.m2.yahoo.com/w/ygo-onesearch%3B_ylt=A0WTc0Lmt1ZMnx4ACwLwOS4J?p=aaron+maxwell&submit=oneSearch&.tsrc=attosus&bzc=19454&.intl=us&.lang=en&lat=40.241337&lon=-74.83738&city=Yardley&street=&state=PA&country=US',
             'searchengine' : 'yahoo',
             'searchphrase' : 'aaron maxwell',
             'is_search' : True,
             },
            {'referrer' : 'http://uk.search.yahoo.com/search?p=latex+.png&ei=utf-8&fr=iobit-trans',
             'searchengine' : 'yahoo',
             'searchphrase' : 'latex .png',
             'is_search' : True,
             },
            {'referrer' : 'http://search.yahoo.com/search;_ylt=A0geu1.LIytMR1sBTgdXNyoA?p=don%C2%B4t+try+to+mount+drive+during+boot+linux+kernel+parameter&fr2=sb-top&fr=yfp-t-701&sao=1',
             'searchengine' : 'yahoo',
             'searchphrase' : 'don´t try to mount drive during boot linux kernel parameter',
             'is_search' : True,
             },
            {'referrer' : 'http://duckduckgo.com/?q=kernel+boot+arguments+ip%3D&v=',
             'searchengine' : 'duckduckgo',
             'searchphrase' : 'kernel boot arguments ip=',
             'is_search' : True,
             },
            {'referrer' : 'http://uk.ask.com/web?q=linux%20kernel%20parameters&o=15527&l=dis&prt=360&chn=retail&geo=GB&ver=4',
             'searchengine' : 'ask',
             'searchphrase' : 'linux kernel parameters',
             'is_search' : True,
             },
            {'referrer' : 'http://www.ask.com/web?qsrc=2990&o=0&l=dir&q=linux+kernel+parameter+to+turn+off+smp',
             'searchengine' : 'ask',
             'searchphrase' : 'linux kernel parameter to turn off smp',
             'is_search' : True,
             },
            # It seems that this is not UTF-8 encoded?
            # {'referrer' : 'http://yandex.ru/yandsearch?text=%e3%e0%e7%ee%e0%ed%e0%eb%e8%e7%e0%f2%ee%f0',
            #  'searchengine' : 'yandex',
            #  'searchphrase' : 'газоанализатор',
            #  'is_search' : True,
            #  },
            {'referrer' : 'http://yandex.ru/yandsearch?clid=9582&text=RedSymbol&lr=213',
             'searchengine' : 'yandex',
             'searchphrase' : 'RedSymbol',
             'is_search' : True,
             },
            ]
        for ii, td in enumerate(testdata):
            ref = Referrer(td['referrer'])
            self.assertEqual(td['referrer'], ref.referrer)
            self.assertEqual(td['is_search'], ref.is_search)
            self.assertEqual(td['searchphrase'], ref.searchphrase)

    def test_nonsearch(self):
        # Path to a giant corpus of referrer strings, one per line
        listing = os.environ['PYREFERRER_NONSEARCH']
        with open(listing) as referrers:
            for referrer in referrers:
                referrer = referrer.strip()
                ref = Referrer(referrer)
                self.assertFalse(ref.is_search, referrer)

if '__main__' == __name__:
    unittest.main()
