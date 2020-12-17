from requests import get
from bs4 import BeautifulSoup

from os import system



def find_synonyms(word):
    """
        This function finds synonyms of a word and return it in list form.
    """

    #get html content of webpage
    response = get(f"https://www.thesaurus.com/browse/{word}")  
    #parse html content
    soup = BeautifulSoup(response.content, 'html.parser')   

    #find the synonyms in the BeautifulSoup Object
    synonyms = soup.find('ul', class_='css-1wdx5pq et6tpn80')

    #remove html tags and extract synonyms from BeautifulSoup object
    #return synonyms in list form
    return [ synonym.get_text() for synonym in synonyms.find_all("li") ]

#To clear terminal
def clear():
    system('cls')

#Main Program
def main():
    """
        The user is prompted to enter a word.
        Synonyms are then shown to the user.
        Screen will be cleared everytime user enter a new word.
    """
    while True:
        try:
            word = input("\nEnter word: ").lower()

            #The program will exit if the user enters space as an input
            if word == " ":
                break

            clear()

            synonyms = find_synonyms(word)
            #every word in synonyms list is printed
            for synonym in synonyms:
                print(synonym)

        except:
            #program restarts if word doesn't exist
            print("Invalid input!")
        
main()
