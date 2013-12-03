#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subtitles2.srtfile

SAMPLE_SRT = """
982
01:27:54,269 --> 01:27:55,394
But most of all ...

983
01:27:55,979 --> 01:27:59,356
 ... I'm tired of that jack-off
and all of his bullshit.
"""

SAMPLE_STRING_CLASSIFICATION = """line number
line number
line time span
dialog lines
dialog lines
line number
line time span
dialog lines
dialog lines
"""


class SrtFileTests(unittest.TestCase):
    def test_lines_classifier(self):
        """Are the srt file lines classified correctly? """
        iterator = SAMPLE_SRT.splitlines().__iter__()
        should_get = SAMPLE_STRING_CLASSIFICATION.splitlines()
        for i, (_, status) in enumerate(subtitles2.srtfile.SrtFile(iterator)):
            self.assertEqual(should_get[i], status, "classifier does not match: expect: '%s' have instead: '%s', position: %d" % (should_get[i], status, i))



if __name__ == '__main__':
    unittest.main()