## Welcome to Subtitles2.py!

**Subtitles2.py** is a python library that makes a search index for the movie and tv show quotes by parsing the `.srt` format files. Under the hood it works by creating a combination of a [Suffix Array](http://en.wikipedia.org/wiki/Suffix_array) and an Inverted index to enable the log-time string matching lookups.

It is very much work in progress at the moment, so please tread gently.

### Example
Let us start with building ourselves a google for **Monty Python and the Holy Grail** quotes. We need to download the repository:
```
git clone https://github.com/dborzov/subtitles2.py
cd subtitles2.py
```
going along with the `examples_grail.py` file:

```python
import subtitles2 #from the subtitles2 folder

src_path = 'srt/Monty Python and the Holy Grail.srt' #path to the .srt file
search_engine = subtitles2.Engine(src_path) #parsing the file and creating the index
```

Now that we created the index, we can do various stuff with it:
```python
print search_engine.query('Ni') # searching for all the string occurences

src_path = 'srt/The Meaning Of Life.srt'
search_engine.parse(src_path) # adding more content to the index
```

That is the basic functionality. Feel free to play with queries or check out more examples exploring various features in the `./examples` folder.

## Directory
Here are the folders contents:

* `./corpus/` contains an sqlite database with the English word vocabulary and usage frequencies for Levenshtein distance 1 typo-corrections;
* `./docs/` library's documentation;
* `./examples` example scripts showcasting various library's features; a good place to start exploring
* `./srt/`, contains example `.srt` that are protected by their owners copyright and should not be used by anybody. Only here for convenience, I will eventually delete this folder.
* `./subtitles2/`, the Python library itself, copy to `$PYTHONPATH/Lib/site-packages/` to use from anywhere in your system.
* `test-subtitles2` library's testing units.

##License
**Subtitles2** is released under the MIT licence.  Contents of `./srt` belong to its owners and should not be downloaded by anyone.
