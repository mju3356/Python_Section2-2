from bs4 import BeautifulSoup
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

html='''
<html>
    <body>
        <h1>파이썬 BeautifulSoup 공부</h1>
        <p>태그 선택자</p>
        <p>CSS 선택자</p>
    </body>
</html>
'''
soup=BeautifulSoup(html,'html.parser')
h1=soup.html.body.h1
p1=soup.html.body.p
p2=p1.next_sibling.next_sibling
p3=p1.previous_sibling.previous_sibling
