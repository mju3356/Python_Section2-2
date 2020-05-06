from bs4 import BeautifulSoup
import sys,io
import urllib.request
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url='https://www.fmkorea.com/football_news'
res=urllib.request.urlopen(url).read()
soup=BeautifulSoup(res,'html.parser')
data=soup.select('#bd_340354_0 > div > table > tbody > tr > td.title.hotdeal_var8 > a:nth-child(1)')
for a in data:
    print(a.get_text().strip())
