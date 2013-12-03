import re


class SrtFile:
    def __init__(self,src_file):
        self.file = open(src_file,'rb')
        self.status = 'line number'
    def next(self):
        line = self.file.next()
        if self.status == 'line number':
            match = re.search('\d+',line)
            if match:
                self.status = 'line time span'
                continue
        elif self.status == 'line time span':
            match = re.search('(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)',line)
            if match:
                self.status = 'dialog lines'
                dialog_line = []
                continue
        elif self.status == 'dialog lines':
            if line == '\r\n':
                self.status = 'line number'
                continue
            dialog_line.append(line)

