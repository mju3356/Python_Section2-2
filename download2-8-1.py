from bs4 import BeautifulSoup
import sys,io
import urllib.request
import urllib.parse
import os
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

base='https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote=urllib.parse.quote_plus('사자')
url=base+quote
#print(url)
res=urllib.request.urlopen(url)
Save_Path='C:/imagedown/'

try:
    if not (os.path.isdir(Save_Path)):
        os.makedirs(os.path.join(Save_Path))
except OSError as e :
    if e.errno != errno.EEXIST:
        print('폴더 만들기 실패!')
        raise
soup=BeautifulSoup(res,'html.parser')
Img_List=soup.select('div.img_area > a.thumb._thumb > img')
print(Img_List)

for i,img_list in enumerate(Img_List,1):
    Full_File_Name=os.path.join(Save_Path+str(i)+'.jpg')
    urllib.request.urlretrieve(img_list['data-source'],Full_File_Name)
print('완료')
