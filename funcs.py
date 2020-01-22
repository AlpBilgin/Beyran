import wikipedia
from colorama import Fore, Back, Style
def emptyLine():
    """Just for empty line."""
    print()

def resultRender(page):
    print(Fore.WHITE + Back.RED + page.title + Style.RESET_ALL)
    print(page.summary)
    print(Fore.YELLOW + "For more information: " + Style.RESET_ALL + page.url)

def pageSelect(searchQuery, selectedPage):
    try:
        if selectedPage != "":
            return wikipedia.page(searchQuery[int(selectedPage)-1])
        else:
            return wikipedia.page(searchQuery[0])
    except ValueError:
        print(Fore.WHITE + Back.RED + "Your value is undefined. You must choose a value between 1 and " + str(len(searchQuery)) + Style.RESET_ALL)
    except wikipedia.DisambiguationError:
        print(Fore.WHITE + Back.RED + "This query has disambugation" + Style.RESET_ALL)
    
def listSearch(searchQuery):
    counter = 0
    for i in searchQuery:
        counter = counter + 1
        print(Fore.RED + str(counter) + ". " + Style.RESET_ALL + i)

def suggestList(suggestList):
    print(type(suggestList))
