from bs4 import BeautifulSoup
import sys,io
import urllib.request
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url='https://finance.daum.net/'
res=urllib.request.urlopen(url).read()
soup=BeautifulSoup(res,'html.parser')

print(soup)
top=soup.select('#boxMarketTrend > div.box_contents > div:nth-child(6) > div:nth-child(1) > ul > li:nth-child(1) > a')
print(top)
