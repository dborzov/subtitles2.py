import unittest
import subtitles2flashcards as testee

class TestFindQoutes(unittest.TestCase):
    def testAdd(self):
        self.assertEqual([], testee.QuoteForAWord('banana', 'How much is the fish?'))

unittest.main()