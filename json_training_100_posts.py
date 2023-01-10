#import requests
#from bs4 import BeautifulSoup
#import openpyxl
#import random

#url='https://jsonplaceholder.typicode.com/posts'
response=requests.get(url)
data=response.json()

book=openpyxl.Workbook()
page=book.active
row=1
for i in data:
    page[f'A{row}'] = i['id']
    page[f'B{row}']=i['title']
    if len(i['title'])>20:
        page[f'C{row}']=len(i['title'])
        page[f'D{row}']="LONG WORDS"
    else:
        page[f'C{row}'] = len(i['title'])
        page[f'D{row}'] = "short WORDS"
    row+=1

book.save(f"{random.randrange(1, 11)}.xlsx")
book.close()








































































