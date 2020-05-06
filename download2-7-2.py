from bs4 import BeautifulSoup
import sys,io
import urllib.request
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url='https://finance.naver.com/sise//'
res=urllib.request.urlopen(url).read().decode('cp949')
soup=BeautifulSoup(res,'html.parser')

top10=soup.select('#popularItemList > li > a')
print(top10)
for i in top10:
    print(i)
#siselist_tab_0 > tbody
