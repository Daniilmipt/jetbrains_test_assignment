import re
import matplotlib.pyplot as plt
import numpy as np
from nltk.stem import WordNetLemmatizer


def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


def my_cool_preprocessor(text, stemmer = WordNetLemmatizer()):
    """ Preprocessing of text """
    text = cleanhtml(text)
    text = text.lower()
    text = re.sub(r'\W', ' ', text)  # remove special chars
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)  # remove alone words
    text = re.sub(r'\d+', ' ', text, flags=re.UNICODE)  # remove digitals

    text = text.split()
    text = [stemmer.lemmatize(word) for word in text]
    return ' '.join(text)


def sort_dict(dc):
    """ Sort dict for values """
    sorted_tuples = sorted(dc.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict


def plot_history(dc, a, b, xtitle):
    k1 = list(dc.keys())[:a]
    v1 = list(dc.values())[:a]
    k2 = k1[:b]
    v2 = v1[:b]
    plt.figure(figsize=(16, 7))
    
    plt.subplot(1, 2, 1)
    plt.suptitle('Frequency of words', fontsize=19, fontweight='bold')
    plt.scatter(x = k1, y = v1, s = 5)
    plt.title(r'The {} most popular words'.format(a), fontsize=15)
    plt.xticks([])
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.title(r'The {} most popular words'.format(b), fontsize=15)
    if not xtitle:
        plt.scatter(x = np.linspace(1, b, b, dtype = 'int'), y = v2, s = 40)
        plt.xlabel('The ordinal number of the word')
    else:
        plt.scatter(x = k2, y = v2, s = 40)
    plt.ylabel('Frequency')
    plt.show()
 

def split_text(text):
    ''' Split text to the sentenses '''
    ls = []
    split_regex = re.compile(r'[.|!|?|…|,]')
    for s in text:
        ls += split_regex.split(s) 
    return ls