import sys
import io
import urllib.request as req
from urllib.parse import urlencode
sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

API='https://api.ipify.org'

values={
    'format':'jsonp
}
params=urlencode(values)
url=API+'?'+params
reqdata=req.urlopen(url).read().decode('utf-8')
print(reqdata)
