from bs4 import BeautifulSoup
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


fp=open('food-list.html',encoding='utf-8')
soup=BeautifulSoup(fp,'html.parser')

print('1',soup.select('li:nth-of-type(4)')[1].string)
print('2',soup.select_one('#ac-list > li:nth-of-type(4)').string)
print('3',soup.select("#ac-list > li[data-lo='cn']")[0].string)
print('4',soup.select('#ac-list > li.alcohol.high')[0].string)

param={'data-lo':'cn','class':'alcohol'}
print('5',soup.find('li',param).string)
print('6',soup.find(id='ac-list').find('li',param).string)
for i in soup.find_all('li'):
    if i['data-lo']=='us':
        print(i.string)
