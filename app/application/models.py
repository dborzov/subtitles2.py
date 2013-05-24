from google.appengine.ext import ndb


class DictionaryWord(ndb.Model):
    """Each real word"""
    word = ndb.StringProperty(required=True)
    frequency = ndb.IntegerProperty(required=True)


class Quote(ndb.Model):
    line = ndb.StringProperty(required=True)
    context = ndb.StringProperty(required=True)
    movie = ndb.StringProperty(required=True)
    youtube = ndb.StringProperty()


class Mention(ndb.Model):
    quote = ndb.KeyProperty(kind=Quote)
    word = ndb.KeyProperty(kind=DictionaryWord)

