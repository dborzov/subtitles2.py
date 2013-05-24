"""
Runs in the AppEngineConsole locally.
"""

SOURCE_PATH = 'c:\Python27\find_this_fucker\'
TARGET = "Terminator.srt"

from google.appengine.ext import ndb
import tramway.srt as srt


sub_text = open(SOURCE_PATH+TARGET, 'r').readlines()
out = srt.srt2movie_lines(sub_text)
open(SOURCE_PATH + 'out.txt', 'w').writelines(out)
print 'whoah, works'
