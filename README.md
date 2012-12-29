## Subtitles-to-cards

**Subtitles-to-cards** parses subtitles' files (*.srt) for word usage statistics and compares it to the general word frequencies of a specific language (English only at the moment). It can then filter target words and make up a nice flash cards with various statistic parameters and context usage quotes.

The idea is to grow foreign language vocabulary by watching movies. 

With this tool one can parse the subtitles' file (*.srt) for a movie before watching and thus
* identify the unknown words 
* sort them in order of general language usage frequency (to learn basic words first and rarely used ones later)
* create printable flashcards with such goodies as context quotes and statistics.

## Usage

Python 2.7 is needed. We run the script with the target file path as an argument:

##License
**Subtitles-to-cards** is released under the MIT licence. 
The license does not cover the general language word usage statistics files (everything in ./corpus/) wich are taken from public sources. 
