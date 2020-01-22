import wikipedia, pyperclip, click
from colorama import Fore, Back, Style
from funcs import emptyLine, resultRender, pageSelect, listSearch, suggestList

# Aranacak argümanı kullanıcıdan alır. İleri sürümlerde argüman olarak da alabilecek
search = input("Please type searched page: " + Fore.YELLOW).title()

# Wikipedia'dan yapılan ilk 10 aramayı bir liste halinde searchQuery değerine aktarır.
searchQuery = wikipedia.search(search)

# listSearch fonksiyonu searchQuery'den aldığı 10 değişkenli listeyi kullanıcıya gösterebilmesi için listSearch fonksiyonuna yollar
listSearch(searchQuery)

# Kullanıcıdan 1 ila 10 arasında bir değer alınarak listedeki değer ile eşlenir.
selectedPage = input("Please choose one of the following options (Press enter for first option)=> " + Fore.YELLOW)

# SelectedPage değişkeninde belirlenen ve okunmak istenen madde query değeri ile beraber pageSelect fonksiyonuna yollanır.
# pageSelect searchQuery içindeki selectedPage'in indeksteki karşılığı olan maddeyi alıp sorgulatır ve ardından hepsini page değişkenine uygular.
page = pageSelect(searchQuery, selectedPage)
emptyLine()

# page değeri içindeki title vb. içerikler düzenlenerek kullanıcının okuyabileceği bir formata getirilir.
resultRender(page)

# Aranan sorgunun Wiki URL'i kullanıcının clipboard'una otomatik olarak yapıştırılır. İleride bu seçenek opsiyonel olacak.
pyperclip.copy(page.url)
print(Fore.RED + "Full URL copied to your clipboard")
