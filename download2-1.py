import sys
import io
import urllib.request as dw
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

imgUrl='https://image.fmkorea.com/files/attach/new/20200415/340354/601189115/2869044769/cdd823e171d49d1e5ed2f65a04731198.jpg'
htmlUrl='http://google.com'
savePath='c:/test1.jpg'
savePath2='c:/index.html'

dw.urlretrieve(imgUrl,savePath)
dw.urlretrieve(htmlUrl,savePath2)
print('다운로드완료!')
