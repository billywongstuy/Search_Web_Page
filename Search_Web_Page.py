from flask import Flask, render_template
#from BeautifulSoup4 import BeautifulSoup
from bs4 import BeautifulSoup 
app = Flask(__name__)
import urllib
import re


#currently only works for the link provided

link = 'https://www.washingtonpost.com/news/the-fix/wp/2016/09/26/the-first-trump-clinton-presidential-debate-transcript-annotated/'
pag = urllib.request.urlopen(link).read()
soup = BeautifulSoup(pag)

page = ([e for e in soup.recursiveChildGenerator() 
         if isinstance(e,str)])

page = str(page)

page = page[page.index("LESTER HOLT:"):page.index("'politics'")-1]



def wordstolist(text):
    selection = []
    word = ''
    text = text.replace('\n',',')
    symbols = ["\'","-"]
    for character in text:
        if ord(character) >= 65 and ord(character) <= 90 or ord(character) >= 97 and ord(character) <= 122 or (character in symbols and len(word) > 0):
            word += character
        else:
            if word != '':
                selection.append(word)
            word = ''
    return selection

def freq(text):
    frequency = {}
    words = wordstolist(text)
    for word in words:
        if word.lower() not in frequency:
            frequency[word.lower()] = 1
        else:
            frequency[word.lower()] += 1
    return frequency

def dictolist(text):
    listee = []
    text2 = freq(text)
    for key, value in text2.items():
        listee.append([value,key])
    listee.sort()
    listee.reverse()
    #listee = listee[:60]
    return listee


searchtext = dictolist(page)
#searchtext = [[1,2],[3,4]]


@app.route("/")
def words():
    return render_template("main.html",content = searchtext,stuff="");
    #return render_template("main.html",content = searchtext,stuff=page);


if __name__ == "__main__":
    app.debug = True
    app.run()


'''
a = open('lit.txt','r')
b = a.read()

def wordstolist(text):
    selection = []
    word = ''
    text = text.replace('\n',',')
    for character in text:
        if ord(character) >= 65 and ord(character) <= 90 or ord(character) >= 97 and ord(character) <= 122:
            word += character
        else:
            if word != '':
                selection.append(word)
            word = ''
    return selection

def freq(text):
    frequency = {}
    words = wordstolist(text)
    for word in words:
        if word.lower() not in frequency:
            frequency[word.lower()] = 1
        else:
            frequency[word.lower()] += 1
    return frequency

def dictolist(text):
    listee = []
    text2 = freq(text)
    for key, value in text2.items():
        listee.append([value,key])
    listee.sort()
    listee.reverse()
    listee = listee[:60]
    return listee


searchtext = dictolist(b)
'''
