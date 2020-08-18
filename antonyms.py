from requests import get
from bs4 import BeautifulSoup

from os import system



def find_antonyms(word):
    """
        This function finds antonyms of a word and return it in list form.
    """

    #get html content of webpage
    response = get(f"https://www.thesaurus.com/browse/{word}")  
    #parse html content
    soup = BeautifulSoup(response.content, 'html.parser')   

    #find the antonyms in the BeautifulSoup Object
    antonyms = soup.find_all('ul', class_ = 'css-17d6qyx-WordGridLayoutBox et6tpn80')[1]

    #remove html tags and extract antonyms from BeautifulSoup object
    #return antonyms in list form
    return [ antonym.get_text() for antonym in antonyms.find_all("li") ]

#To clear terminal
def clear():
    system('cls')

#Main Program
def main():
    """
        The user is prompted to enter a word.
        antonyms are then shown to the user.
        Screen will be cleared everytime user enter a new word.
    """
    while True:
        try:
            word = input("\nEnter word: ").lower()

            #The program will exit if the user enters space as an input
            if word == " ":
                clear()
                print("Program Exit...")
                break
            
            #clear screen for less clutter
            clear()

            antonyms = find_antonyms(word)
            #every word in antonyms list is printed
            for antonym in antonyms:
                print(antonym)

        except:
            #program restarts if word doesn't exist
            print("Invalid input!")

main()
