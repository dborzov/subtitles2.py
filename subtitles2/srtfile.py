"""
Contains SrtFile, an iterator supposed to go through the .srt formatted text and classify the type of each line (line number, the dialogue time or the dialogue itself).
"""

import re
import datetime


class SrtFile(object):
    """
    Iterates through st file line by line
    """
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


class SrtIterator(object):
    """
    Iterates through each entry in the srt file
    """
    def __init__(self,iterator):
        self.iterator = iterator
        self.StopIterator = False

    def __iter__(self):
        return self

    def next(self):
        self.status = 'line number'
        if self.StopIterator:
            """ Last time we reached the end of source, time to stop iteration"""
            raise StopIteration

        dialog = '' # preassign only for when zero readings before reaching end of source
        time_start = datetime.timedelta(0)# that is, the source is really not an .srt
        time_end = datetime.time(0)# that is, the source is really not an .srt

        while True:
            try:
                line = self.iterator.next()
            except:
                self.StopIterator = True
                break
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
                    time_start = datetime.timedelta(0, int(sec), 0, int(microsec),  int(minute), int(hour))
                    hour, minute, sec, microsec = match.group(5,6,7,8)
                    time_end = datetime.timedelta(0, int(sec), 0, int(microsec), int(minute), int(hour))
                    self.TimeSpan = time_end # keeps track of the overall film's timespan
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
