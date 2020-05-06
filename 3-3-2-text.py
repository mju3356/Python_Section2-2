import sys,io
import requests
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


r=requests.get('http://openapi.tago.go.kr/openapi/service/TrainInfoService?_wadl&_type=xml')
print(r.text)
