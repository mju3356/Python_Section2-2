import sys
import io
import urllib.request as req
from urllib.parse import urlparse
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url='https://www.naver.com/'
mem=req.urlopen(url)

#print('geturl',mem.geturl())
#print('status',mem.status)
#print('hearders',mem.getheaders())
#print(mem.info())
#print('code',mem.getcode())

#print('read',mem.read().decode('utf-8'))
print(urlparse(url))
