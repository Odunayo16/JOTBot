from bs4 import BeautifulSoup
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy
from numpy import array
from collections import Counter
from nltk import word_tokenize as wt
# import lxml

LEN = 72

def get_vec(message):
    vec = []
    for i in range(0, LEN):
        vec.append(0);
    toks = message.split()
    for tok in toks:
        if keywords.has_key(tok):
            # t = vec(keywords[tok])
            # t += 1
            t = keywords[tok]
            vec[t]+=1
    l = float(len(toks))
    for i in range(0, LEN):
        vec[i] = vec[i] / l 
    return vec

#stackoverflow
def unit_vec(vec):
    return vec / numpy.linalg.norm(vec)

#stackoverflow
def angle_cos(v1, v2):
    v1u = unit_vec(v1)
    v2u = unit_vec(v2)
    return numpy.clip(numpy.dot(v1u, v2u), -1.0, 1.0)

# find the closest vector to v1
def find_closest(v1):
    maxcos = 0
    closest = None
    for cat in categories:
        a = angle_cos(v1, categories[cat])
        if a > maxcos:
            maxcos = a
            closest = cat
    return closest


keywords = {'Bible': 0, 'Christian': 1, 'Christians' : 2, 'Jesus' : 3, 'God' : 4, 'bible' : 5, 'pray' : 6, 'Christ' : 7, 'faith' : 8, 'belief' : 9, 'calcium' : 10, 'risk' : 11, 'supplements' : 12, 'lifespan' : 13, 'lines' : 14, 'Calcium' : 15, 'article' : 16, 'years' : 17, 'body' : 18, 'disease' : 19, 'Catholic' : 20, 'salvation' : 21, 'Testament' : 22, 'righteousness' : 23, 'interpretation' : 24, 'sin' : 25, 'worship' : 26, 'iPhone' : 27, 'Intel' : 28, 'Leopard' : 29, 'PowerPC' : 30, 'Macs' : 31, 'Apple' : 32, 'Mac' : 33, 'OS' : 34, 'computer' : 35, 'Safari' : 36, 'AppleCare' : 37, 'iPod' : 38, 'Macbook' : 39, 'MacBook' :40, 'philosophy' : 41, 'mathematics' : 42, 'dead' : 43, 'dreaming' : 44, 'good' : 45, 'concept' : 46, 'think' : 47, 'question' : 48, 'reality' : 49, 'sufficient' : 50, 'exists' : 51, 'suicide' : 52, 'death' : 53, 'consciousness' : 54, 'baking' : 55, 'recipe' : 56, 'brown' : 57, 'bacon' : 58, 'sheet' : 59, 'sugar' : 60, 'cream' : 61, 'soda' : 62, 'powder' : 63, 'oven' : 64, 'sauce' : 65, 'eggs' : 66, 'cooked' : 67, 'fat' : 68, 'food' : 69, 'and' : 70, 'the' : 71}

categories = {}

def frequency_print(filename):
    DOMTree = xml.dom.minidom.parse(filename + ".xml")
    collection = DOMTree.documentElement
    posts = collection.getElementsByTagName("row")

    text = []
    i = 0
    for post in posts:
        if i > 500: break
        text.append(post.getAttribute("Body"))
        i = i + 1

    rawtext = "".join(text)
    cleantext = BeautifulSoup(rawtext, 'html.parser')
    cleantext = cleantext.get_text()
    splittext = wt(cleantext)
    counts = Counter(splittext)
    """print ""
    print filename
    for word, count in counts.most_common(200):
        print '%s: %7d' % (word, count)"""
    
    categories[filename] = get_vec(cleantext)

frequency_print("Health")
frequency_print("Christianity")
frequency_print("Apple")
frequency_print("Philosophy")
frequency_print("Cooking")

"""DOMTree = xml.dom.minidom.parse("Christianity.xml")
collection = DOMTree.documentElement
posts = collection.getElementsByTagName("row")

text = []
i = 0
for post in posts:
    if i > 25: break
    text.append(post.getAttribute("Body"))
    i += 1

rawtext = "".join(text)
cleantext = BeautifulSoup(rawtext, 'html.parser')
cleantext = cleantext.get_text()

categories["Christianity"] = get_vec(cleantext)"""

"""splittext = wt(cleantext)
counts = Counter(splittext)
print counts"""

#vec1 = [1, 2]
#vec2 = [2, -1]
#print unit_vec(vec1)
#print unit_vec(vec2)
#print angle_cos(vec1, vec2)

while True:
    q = raw_input("usr: ")
    if q is "bye": break;
    v = get_vec(q)
    print find_closest(v)
