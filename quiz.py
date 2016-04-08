from bs4 import BeautifulSoup
import requests

# intialize lists for storing findings

def printAll(listName):
    for item in listName:
        print(item)

def getCards(inputUrl):
    cardSet = {
        'terms' : [],
        'definitions' : []
    }

    # set up beautiful soup
    r = requests.get(inputUrl)
    soup = BeautifulSoup(r.content, "html.parser")

    # pull term data
    termTag = soup.find_all("span",{"class": "TermText qWord lang-en"})
    for item in termTag:
        cardSet['terms'].append(item.text)

    defTag = soup.find_all("span",{"class": "TermText qDef lang-en"})
    for item in defTag:
        cardSet['definitions'].append(item.text)

    return cardSet

def getMneumonics(term):
    mneumonics = []

    # set up beautiful soup
    url = "http://www.mnemonicdictionary.com/?word=" + term
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    defTag = soup.find_all("div",{"class" : "span9"})

    if len(defTag) == 0:
        return ['No mneumonics for this word.']
    else:
        for x in xrange(0,len(defTag)):
            if x+1 == len(defTag):
                mneumonics.append((defTag[x].text).replace("   ","").replace("\n","").replace("\r",""))
                return mneumonics
            elif x < 3:
                mneumonics.append((defTag[x].text).replace("   ","").replace("\n","").replace("\r",""))


# ==========================  BEGIN MAIN FUNCTION   ============================
### FOR DEBUGGING:
# url = "https://quizlet.com/247919/vocabulary-workshop-level-g-unit-13-flash-cards/"
###
print("""  ___        _     _
 / _ \ _   _(_)___| |    ___  __ _ _ __ _ __
| | | | | | | |_  / |   / _ \/ _` | '__| '_ \\
| |_| | |_| | |/ /| |__|  __/ (_| | |  | | | |
 \__\_\\\__,_|_/___|_____\___|\__,_|_|  |_| |_|

""")
url = raw_input("Please paste the URL to the quizlet.\n > ")
print("Searching...\n\n")

cardSet = getCards(url)

for x in xrange(0,len(cardSet['terms'])):
    print(cardSet['terms'][x] + ":\n------------")
    print(cardSet['definitions'][x] + "\n")
    printAll(getMneumonics(cardSet['terms'][x]))
    print("\n")

print("\n\nThank you for using QuizLearn! Goodbye! :)")

# printAll(mneumonics)
# =========================   END MAIN FUNCTION   ==============================
