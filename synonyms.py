from requests import get
from bs4 import BeautifulSoup

from os import system, name

def clear():
    system('cls')

def find_synonyms(word):
    response = get(f"https://www.thesaurus.com/browse/{word}")
    soup = BeautifulSoup(response.content, 'html.parser')

    # synonyms = soup.select('.css-umlvd6-MainContentContainer > .css-1e8kf7o-CenterContentContainer > .css-191l5o0-ClassicContentCard > .css-17d6qyx-WordGridLayoutBox')
    synonyms = soup.find(attrs = {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})

    # print (f'\nSynonyms for {word}')

    # for synonym in synonyms.find("ul"):
    #     print(synonym.get_text())

    return [ synonym.get_text() for synonym in synonyms.find("ul") ]

def main():

    while True:
        try:
            word = input("\nEnter word: ").lower()
            if word == " ":
                break
            clear()
            synonyms = find_synonyms(word)
            for synonym in synonyms:
                print(synonym)
        except:
            print("Invalid input!")
        
    
    
main()
