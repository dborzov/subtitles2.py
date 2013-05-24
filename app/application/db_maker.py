"""
Runs in the AppEngineConsole locally.
"""

SOURCE_PATH = # gotta set it up

from google.appengine.ext import ndb


class DictionaryWord(ndb.Model):
    """Example Model"""
    word = ndb.StringProperty(required=True)
    frequency = ndb.IntegerProperty(required=True)


word_corpus=open(SOURCE_PATH,"rb").readlines()

for frequency, word in enumerate(word_corpus):
    new_entry = DictionaryWord()
    new_entry.word = word.rstrip()
    new_entry.frequency = frequency+1
    new_entry.put()