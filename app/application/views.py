import json
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache
import texter
from application import app
from decorators import login_required, admin_required
from models import DictionaryWord, Mention
import re
from collections import Counter
import logging


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def parser(word):
    """ individual word into array of dicts
    of quotes """
    dict_match = DictionaryWord.query(
            DictionaryWord.word == word).fetch()
    if dict_match:
        mentions = Mention.query(Mention.word == dict_match[0].key).fetch()
        yeild_text = []
        for mention in mentions:
            quote = mention.quote.get()
            quote_dict = {'line':quote.line,
                        'context': quote.context,
                        'movie':quote.movie
                        }
            yeild_text.append(quote_dict)
        return yeild_text
    else:
        return []


def prioritize(words):
    counters = {}
    for word in words:
        dict_match = DictionaryWord.query(
            DictionaryWord.word == word).fetch()
        if dict_match:
            mentions = Mention.query(Mention.word == dict_match[0].key).fetch()
            for mention in mentions:
                if mention.quote in counters:
                    counters[mention.quote] += 1
                else:
                    counters.update(dict([(mention.quote, 1)]))
    ordered = sorted(counters.items(), key=lambda x: x[1]).copy()
    logging.debug(" ====================================== ")
    logging.debug(ordered)
    logging.debug(" ====================================== ")
    return ordered


def retriever(keys):
    yeild_dicts = []

    for key in keys:
        quote = key.get()
        quote_dict = {'line':quote.line,'context':quote.context,'movie':quote.movie}
        yeild_dicts.append(quote_dict)
    return yeild_dicts


def say_hello():
    query = json.loads(request.data)
    words = texter.words_from_string(query["query"])
    #keys = parser(word)
    #out = retriever(keys)
    out = []
    for word in words:
        out += parser(word)
    if not out:
        out = [{'line': '', 'context': '<h1>:/</h1>Nothing found', 'movie': ''}]
    return json.dumps(out)





def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

