import json
import requests
import re
from bs4 import BeautifulSoup

startNumber = 23000
endNumber = 24000
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)


for i in range(startNumber, endNumber):

    try:

        url = 'https://travaillerpour.be/fr/job/?jobcode=AFG' + str(i)
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            scriptJson = soup.find('div', attrs={'class': 'node__header--bottom'})
            title = soup.find('h1', attrs={'class': 'node__title'})
            company = soup.find('span', attrs={'class': 'organization-name'})
            offers = soup.find('div', attrs={'class': 'field__item'})
            dateLimite = soup.find('span', attrs={'class': 'apply-till-date'})
            if scriptJson is not None :
                listData = remove_tags(scriptJson.text)
                listTitle=remove_tags(title.text)
                listCompany=remove_tags(company.text)
                listOffers = remove_tags(offers.text)
                listDate = remove_tags(dateLimite.text)
                deleteLines=":".join(listData.splitlines()).replace(":::","\n").replace("::",":").replace(":T","T").replace("externe\n:","externe\n")

                print(f"Fonction : {listTitle}")
                print(deleteLines)
                print(f"Société : {listCompany}")
                print(f"Nombre de poste : {listOffers} ")
                print(f"Date Limite : {listDate} ")
                print("-----------------------------------------------------------------------------------------------------------------------------")

    except ValueError:
        print("Decoding JSON has failed")
        print("--------------------------------------------------------------------------------------------------")
