import matplotlib.pyplot as plt
import PyPDF2
import textract
import warnings
warnings.filterwarnings("ignore")
# import nltk
from nltk.tokenize import word_tokenize
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
filename = askopenfilename()
print(filename)
# nltk.download('punkt')
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
if text != "":
    k=1
    text = text
else:
    print("text is empty")
    k=0
    # text = textract.process(fileurl, method='tesseract', language='eng')
tokens = word_tokenize(text)
try:
    tokens.remove(".")
except:
    print()
punctuations = ['(',')',';',':','[',']',',',' ',"'",'.',"''",'+','-','=','*','/',"!","@","#",'’',"$","%","^","&","(",")","?",'...',"-","`",'‘',"``","--","1","2","3","4","5","6","7","8","9","0"]
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
if k:
    keywords = [porter.stem(word.lower()) for word in tokens if not word in punctuations]
    keyset=set(keywords)
    di={}
    for i in keyset:
        di[i]=keywords.count(i)
    l = sorted(di.items(), key=lambda kv: (kv[1], kv[0]), reverse = True)
    print(l[0:10])
    rdic={}
    for i in l[0:10]:
        rdic[i[0]]=i[1]
    plt.bar(list(rdic.keys()), rdic.values(), color='g')
    plt.title(filename)
    plt.show(block=False)
    plt.pause(10)
    plt.close()
