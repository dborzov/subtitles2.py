import unittest
import texter


class TexterTests(unittest.TestCase):
    known_results = (('reward love', ['reward', 'love']),
                    ('obey groom', ['obey', 'groom']))
    def test_known(self):
        for string, array in self.known_results:
            result = texter.words_from_string(string)
            self.assertEqual(array, result)




if __name__ == "__main__":
    unittest.main()