"""
Contains SrtFile, an iterator supposed to go through the .srt formatted text and classify the type of each line (line number, the dialogue time or the dialogue itself).
"""

import re


class SrtFile:
    def __init__(self,iterator):
        self.iterator = iterator
        self.status = 'line number'

    def __iter__(self):
        return self

    def next(self):
        line = self.iterator.next()
        line_status = self.status
        if self.status == 'line number':
            match = re.search('\d+',line)
            if match:
                self.status = 'line time span'
        elif self.status == 'line time span':
            match = re.search('(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)',line)
            if match:
                self.status = 'dialog lines'
        elif self.status == 'dialog lines':
            match = re.search('\w',line)
            if not match:
                self.status = 'line number'
        return line, line_status

