import os, re, argparse, sys

VOCABULARY_CORPUS_PATH="corpus/corpus.txt"
LOWER_LIMIT=100
HIGHER_LIMIT=7000


# Clears off meta/non-text strings in the .str file format
def RenderSrtFile(sub_text):
    out=[]
    for each_line in sub_text:
        if "-->" not in each_line:
            if not re.search(r'\w',each_line)==None:
                if re.search(r'^\d',each_line)==None:
                    out.append(each_line)
    return out


# Separates individual words
def WordsFromText(Text_Lines):
    word_array=[]
    for each_line in Text_Lines:
        words=re.findall(r'\w+',each_line)
        for each_word in words:
            word_array.append(each_word.lower())
    return word_array


# Transforms an array of words into the set ordered in the occurance frequency
def CountWordFrequency(word_array):
    unique_words=set(word_array)
    unsorted_word_frequencies=[(a_word,word_array.count(a_word)) for a_word in unique_words]
    word_frequencies=sorted(unsorted_word_frequencies,key=lambda x:(-1)*x[1])
    return word_frequencies


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






if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Word statistics for subtitles' (.srt) files")
    try:
        file_name=sys.argv[1]
        print file_name, 'is taken as the target file.'
    except:
        print "Woops, put some .srt file as an argument."
        sys.exit()

    print "checking file ", file_name
    if file_name[-3:]=="srt":
        try:
            sub_text=open(file_name,'r').readlines()
        except:
            print "Cannot open the file"
            sys.exit()
        out=RenderSrtFile(sub_text)
        words=WordsFromText(out)
        word_frequencies=CountWordFrequency(words)
        identified_words=IdentifyWords(word_frequencies,LOWER_LIMIT,HIGHER_LIMIT)
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



