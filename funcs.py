import wikipedia, os
from colorama import Fore, Back, Style

def emptyLine():
    """Just for empty line."""
    print()

def error(message):
    print(Fore.WHITE + Back.RED + message + Style.RESET_ALL)

def exportPage( page):
    exportFile = open(page.title + ".txt", "w")
    pageArray = page.content.split("\n")
    for i in pageArray:
        exportFile.writelines(i)
    
    exportFile.close()
    error("Article exported")

def fullPage(page):
    pageArray = page.content.split("\n")
    for i in pageArray: 
        if i[0:3] == "== " or i[0:3] == "===": 
            if i[0:3] == "==":
                print(Fore.RED + i.upper() + Style.RESET_ALL)
            else:
                print(Fore.RED + i + Style.RESET_ALL) 
        else:
            print(i)
    textQuestion = input("Do you want to export this article? (y / n): " + Fore.YELLOW + Style.RESET_ALL)
    if textQuestion == "y":
        exportPage(page)
    else:
        exit
    
                   
def resultRender(page):
    os.system("clear")
    try:
        print(Fore.WHITE + Back.RED + page.title + Style.RESET_ALL)
        exit
    except AttributeError:
        error("A problem occured")
    
    try:
        if page.coordinates != None:
            lat = str(round(page.coordinates[0], 2))
            lon = str(round(page.coordinates[1], 2))
            print(Fore.RED + "Coordinates: " + Style.RESET_ALL + lat + ", " + lon)
        else:
            pass
    except KeyError:
        pass

    print(page.summary)
    emptyLine()
    print(Fore.YELLOW + "For more information: " + Style.RESET_ALL + page.url)
    fullQuestion = input("Do you want to see full page? (y/n): ")
    if fullQuestion == "y":
        os.system("clear")
        fullPage(page)
    else:
        exit


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
    os.system("clear")
    counter = 0
    for i in searchQuery:
        counter = counter + 1
        print(Fore.RED + str(counter) + ". " + Style.RESET_ALL + i)

def mahmut():
    resultRender(wikipedia.page("Mahmud"))
    exit
    
