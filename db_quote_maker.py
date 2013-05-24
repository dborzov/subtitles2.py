"""
Runs in the AppEngineConsole locally.
"""
# from google.appengine.ext import ndb
import srt


h = 3
SOURCE_PATH = "sub/"
TARGET = "Terminator.srt"



sub_text = open(SOURCE_PATH+TARGET, 'r').readlines()
out = srt.srt2movie_lines(sub_text)
open(SOURCE_PATH + 'out.txt', 'w').writelines(out)
print 'whoah, works'
