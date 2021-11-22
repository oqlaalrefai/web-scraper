import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(URL):
    '''it counting the citation needed in the paragraphs'''
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,"html.parser")
    result = soup.find("div",id="mw-content-text") 
    citations_needed = result.find_all(title='Wikipedia:Citation needed',limit=None)

    return len(citations_needed)


    
def get_citations_needed_report(URL):
    '''This function accept an url and scrap the data from it, then, its reporting the citaion needed'''
    finalString = ''
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,"html.parser")
    citations_needed = soup.find_all(class_="noprint Inline-Template Template-Fact")


    for i in citations_needed:
        text = i.find_parent('p').get_text()
        finalString += text + '\n'

    return finalString

if __name__ == '__main__':
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))