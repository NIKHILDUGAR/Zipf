import matplotlib.pyplot as plt
import PyPDF2
import re
from operator import itemgetter
import textract
import warnings

warnings.filterwarnings("ignore")
import nltk
from nltk.tokenize import word_tokenize
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
print(filename)
nltk.download('punkt')
frequency = {}
try: #if file is pdf
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()
    if text != "":
        k = 1
        text = text
    else:
        print("text is empty")
        k = 0
        # text = textract.process(fileurl, method='tesseract', language='eng')
    tokens = word_tokenize(text)
    try:
        tokens.remove(".")
    except:
        print()
    punctuations = ['p', 'x', '}', '{', '(', ')', '”', ">", "<", ';', ':', '[', ']', ',', ' ', "'", '.', "''", '“', '+',
                    '-', '=', '*', '/', "!", "@", "#", '’', "$", "%", "^", "&", "(", ")", "?", '...', "-", "`", '‘',
                    "``", "--", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    from nltk.stem.porter import PorterStemmer

    porter = PorterStemmer()
    if k:
        keywords = [porter.stem(word.lower()) for word in tokens if not word in punctuations]
        keyset = set(keywords)

        for i in keyset:
            frequency[i] = keywords.count(i)
        l = sorted(frequency.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        print(l[0:10])
        rdic = {}
        for i in l[0:10]:
            rdic[i[0]] = i[1]
        plt.bar(list(rdic.keys()), rdic.values(), color='g')
        plt.title(filename)
        plt.show(block=False)
        try:
            plt.pause(200)
            plt.close()
        except:
            print()
except:
    # trying to read a txt file
    open_file = open(filename, 'r')
    file_to_string = open_file.read()
    words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)
    for word in words:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
        l = sorted(frequency.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        print(l[0:10])
        rdic = {}
        for i in l[0:10]:
            rdic[i[0]] = i[1]
        plt.bar(list(rdic.keys()), rdic.values(), color='g')
        plt.title(filename)
        plt.show(block=False)
        try:
            plt.pause(200)
            plt.close()
        except:
            print()
