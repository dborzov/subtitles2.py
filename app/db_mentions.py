"""
Runs in the AppEngineConsole locally.
"""
import texter

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



def reset():
    all_lines = Quote.query().fetch()

    ti = 'Hiyo'
    for line in all_lines:
        for piece in texter.words_from_string(line.line):
            is_a_word = DictionaryWord.query(DictionaryWord.word == piece).fetch()
            if is_a_word:
                new_mention = Mention()
                new_mention.quote = line.key
                new_mention.word = is_a_word[0].key
                new_mention.put()
    return ti

def flush():
    """deletes all the mention records in database."""
    all_mentions = Mention.query().fetch()
    for mention in all_mentions:
        mention.delete()
    return 'The deed is done, all mentions are deleted'


def right_name():
    """deletes all the mention records in database."""
    all_lines = Quote.query().fetch()
    for quote in all_lines:
        quote.movie = 'Monty Python and the Holy Grail'
        quote.put()
    return 'The deed is done!'

def rectify():
    """deletes all the mention records in database."""
    all_lines = Quote.query().fetch()
    for quote in all_lines:
        quote.context.replace('\n', ' \n<br>')
        quote.put()
    return 'The rectifying is done!'
