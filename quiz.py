from bs4 import BeautifulSoup
import requests

# intialize lists for storing findings
terms = []
definitions = []
mneumonics = []


def printAll(listName):
    for item in listName:
        print(item)

def getCards(inputUrl):
    # set up beautiful soup
    r = requests.get(inputUrl)
    soup = BeautifulSoup(r.content, "html.parser")

    # pull term data
    termTag = soup.find_all("span",{"class": "TermText qWord lang-en"})
    for item in termTag:
        terms.append(item.text)

    defTag = soup.find_all("span",{"class": "TermText qDef lang-en"})
    for item in defTag:
        definitions.append(item.text)

    printAll(terms)
    print("\n================================\n")
    printAll(definitions)
    print("\n================================\n")

def getMneumonics(term):
    # set up beautiful soup
    url = "http://www.mnemonicdictionary.com/?word=" + term
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    defTag = soup.find_all("div",{"class" : "span9"})

    if len(defTag) == 0:
        print("No mneumonics for this word.")

    for x in xrange(0,len(defTag)):
        tempMneumonic = ""
        if x < 3:
            print (defTag[x].text).replace("   ","").replace("\n","")
            # removing some of this due to the fact that some definitions are
            # encoded fairly strangely
            # mneumonics.append(str(defTag[x].text).replace("   ","").replace("\n",""))
        else:
            mneumonics.append("\n")
            break

# ==========================  BEGIN MAIN FUNCTION   ============================
# url = raw_input("Please paste the URL to the quizlet.\n > ")

# for the purpose of debugging, we shall have it be this URL for now.
url = "https://quizlet.com/27467/sadlier-oxford-vocabulary-level-g-unit-11-flash-cards/"
getCards(url)
for x in xrange (0,len(terms)):
    print(terms[x] + ":")
    print(definitions[x])
    print("\n")
    getMneumonics(terms[x])
    percent = float(x)/float(len(terms)) * 100
    print("==============================")
    # print(str(percent)+"%")

print("\n\nThank you for using QuizLearn! Goodbye! :)")

# printAll(mneumonics)
# =========================   END MAIN FUNCTION   ==============================
