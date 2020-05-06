import sys,io
import requests
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


s=requests.session()
r=s.get('http://httpbin.org/get')
#print(r.status_code)
#print(r.ok)
#수정

#https://jsonplaceholder.typicode.com/

r=s.get('https://jsonplaceholder.typicode.com/posts/1')
