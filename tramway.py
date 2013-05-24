import argparse
import sys
import srt
import texter


VOCABULARY_CORPUS_PATH="corpus/corpus.txt"
LOWER_LIMIT=100
HIGHER_LIMIT=7000


# identifies words in the corpus and assigns their rank
def IdentifyWords(word_frequencies, lower_limit,higher_limit):
    corpus=[line[:-1] for line in open(VOCABULARY_CORPUS_PATH,'r').readlines()]
    identified_words=[word for word in word_frequencies if word[0] in corpus]
    identified_array=[]
    for unique_word in identified_words:
        rank=corpus.index(unique_word[0])
        if rank>lower_limit and rank<higher_limit:
            identified_array.append((unique_word[0],unique_word[1],rank+1))
    return identified_array


# finds an example of the word usage
def Quote_For_A_Word(word,textbody):
    return 'Hi!'


def RenderFile(file_name):
    print "checking file ", file_name
    if file_name[-3:]=="srt":
        try:
            sub_text=open(file_name,'r').readlines()
        except:
            print "Cannot open the file"
            sys.exit()

        out = srt.srt2movie_lines(sub_text)
        words = srt.WordsFromText(out)
        word_frequencies = texter.CountWordFrequency(words)
        identified_words = IdentifyWords(word_frequencies,LOWER_LIMIT,HIGHER_LIMIT)
        card_tuple=[word+(Quote_For_A_Word(word[0],sub_text),) for word in identified_words]

        out_file=open(file_name[:-3]+'txt',"w")
        out_file.writelines(out)
        out_file.close()

        out_file=open(file_name[:-3]+'words',"w")
        for each_word in words:
            out_file.write(each_word+'\n')
        out_file.close()

        out_file=open(file_name[:-3]+'frequencies',"w")
        for unique_word in word_frequencies:
            out_file.write(str(unique_word[0])+', count:'+str(unique_word[1])+'\n')
        out_file.close()

        out_file=open(file_name[:-3]+'ranking',"w")
        for unique_word in identified_words:
            out_file.write(str(unique_word[0])+', count:'+str(unique_word[1])+', rank:'+str(unique_word[2])+'\n')
        out_file.close()

        out_file=open(file_name[:-3]+'cards',"w")
        for unique_word in card_tuple:
            out_file.write('==================================\n')
            out_file.write(unique_word[0]+'\n')
            out_file.write('Usage count:'+str(unique_word[1])+'\n')
            out_file.write('Word rank:'+str(unique_word[2])+'\n')
            out_file.write('Quote:'+str(unique_word[3])+'\n')
        out_file.write('==================================\n')
        out_file.close()

        print("Done.")


if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Word statistics for subtitles' (.srt) files")
    try:
        file_name=sys.argv[1]
        print file_name, 'is taken as the target file.'
        RenderFile(file_name)
    except:
        print "Woops, put some .srt file as an argument."
        sys.exit()



