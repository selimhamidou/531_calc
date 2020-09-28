from bs4 import BeautifulSoup
from urllib.parse import urlencode
import requests
import string

def myfitnesspal_parser():
    search_url='https://www.myfitnesspal.com/fr/food/search?'
    cookies = dict(BCPermissionLevel='PERSONAL')
    html = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies)
    pages=range(50)
    array=[]
    alphabet=string.ascii_lowercase
    for letter in alphabet:
        array.append(letter)
    #print(array)
    test=open("text.txt",'w')
   
    for letter in array:
        for page in pages:
            params={'search':letter}
            response = requests.get(search_url + 'page=' + str(page) + '&search=' + urlencode(params))
            soup = BeautifulSoup(response.text, 'html.parser')
            for element in range(0, len(soup.find_all(class_='jss8'))):
                #print(soup.find_all(class_='jss8')[element].text)
                #print(soup.find_all(class_='jss14')[element].text)
                test.write(soup.find_all(class_='jss8')[element].text)
                test.write(soup.find_all(class_='jss14')[element].text)

myfitnesspal_parser()

