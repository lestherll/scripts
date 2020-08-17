from requests import get
from bs4 import BeautifulSoup

from os import system


def find_definition(word, limit = False):
    """
    This function returns a list of a definition of a word

    Parameters
    ----------
    word : str
        The function will lookup the meaning of word        
    limit : int, optional
        This is the limit of definitions that will be returned
        Default limit is 5
    """

    #default value for limit is set to 5
    limit = 5 if limit is False else limit

    #extract and parse html content from url
    url = "http://dictionary.cambridge.org/dictionary/british/" + word.lower()
    response = get(url, headers={"User-Agent":"Mozilla/5.0"})  
    soup = BeautifulSoup(response.content, "html.parser")  

    #extract definition
    definitions = soup.find_all("div", class_="def ddef_d db")
    
    #return definitions in list form
    return [definition.text.replace(":", "") for definition in definitions[:5]]


def display_word_def(word):
    """
    This function displays the meaning/s of a word 
    in a comprehensible format
    """

    #call find_definition function to look up meaning of word
    #limit=some_number can be used as a parameter to set no. of definitions returned
    definitions = find_definition(word)

    #format the display
    print("\n", word.upper())
    [print("- ", definition) for definition in definitions]
    print("")


def main():
    
    #loop for continuous prompt
    while True:
        try:

            #input word to look up
            word = input("Look for meaning of: ")
            
            #break program when space is entered
            if word == " ":
                break
            
            #clear screen to avoid clutter
            system("cls")
            
            #display word definiton
            display_word_def(word)

        except AttributeError:
            print("INVALID INPUT")

#MAIN PROGRAM
main()

