from google.appengine.ext import ndb


class DictionaryWord(ndb.Model):
    """Example Model"""
    word = ndb.StringProperty(required=True)
    frequency = ndb.IntegerProperty(required=True)