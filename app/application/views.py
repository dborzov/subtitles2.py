import json
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from models import DictionaryWord
import tramway.texter as srt
import re


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)



def say_hello():
    query = json.loads(request.data)
    dict_match = DictionaryWord.query(
            DictionaryWord.word == query['query']).fetch()
    if dict_match:
        return dict_match[0].word + ' ,freq:' + str(dict_match[0].frequency)
    else:
        return ", ".join(srt.words_from_string(query['query']))



def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

