"""
Contains SrtFile, an iterator supposed to go through the .srt formatted text and classify the type of each line (line number, the dialogue time or the dialogue itself).
"""

import re
import datetime


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


class SrtIterator:
    def __init__(self,iterator):
        self.iterator = iterator

    def __iter__(self):
        return self

    def next(self):
        self.status = 'line number'
        while True:
            line = self.iterator.next()
            if self.status == 'line number':
                match = re.search('\d+',line)
                if match:
                    self.status = 'line time span'
                    continue
            elif self.status == 'line time span':
                match = re.search('(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)',line)
                if match:
                    # We stumbled upon timespan line, get ready to read dialogue itself
                    hour, minute, sec, microsec = match.group(1,2,3,4)
                    time_start = datetime.time(int(hour), int(minute),int(sec), int(microsec))
                    hour, minute, sec, microsec = match.group(5,6,7,8)
                    time_end = datetime.time(int(hour), int(minute),int(sec), int(microsec))
                    self.status = 'dialog lines'
                    dialog = ''
                    continue
            elif self.status == 'dialog lines':
                match = re.search('\w',line)
                if match:
                    dialog +=line
                else:
                    # we stumbled upon an empty string, means end of dialog lines
                    break
        return time_start, time_end, dialog
