"""
MIT lisense, written by Dima Borzov

The project source code is available at:
gihub.com/dborzov/tramway
------------------------------
srt.py:
All the srt-format specific processing operations.
"""

import re


def srt2movie_lines(sub_text):
    """
    Clears off meta/non-text strings in the .str file format.
    Yields movie lines as a text.
     """
    out=[]
    for each_line in sub_text:
        if "-->" not in each_line:
            if not re.search(r'\w', each_line) is None:
                if re.search(r'^\d', each_line) is None:
                    out.append(each_line)
    return out



def WordsFromText(Text_Lines):
    """ Separates individual words from an array of text lines. """
    word_array=[]
    for each_line in Text_Lines:
        words=re.findall(r'\w+', each_line)
        for each_word in words:
            word_array.append(each_word.lower())
    return word_array



