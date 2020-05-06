from bs4 import BeautifulSoup
import sys,io
import urllib.request
import urllib.parse
import os
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

base='https://www.inflearn.com/'
quote=urllib.parse.quote_plus('')
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
Img_List=soup.select('div.course_card_item')
print(Img_List)

for i,img_list in enumerate(Img_List,1):
    with open(Save_Path+'text_'+str(i)+'.txt','wt') as f:
        f.write(img_list.select_one('div.course_title').string)
    Full_File_Name=os.path.join(Save_Path,Save_Path+str(i)+'.jpg')
    urllib.request.urlretrieve(img_list.select_one('div.card-image > figure > img')['src'],Full_File_Name)

print('완료')
