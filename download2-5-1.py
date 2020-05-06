from urllib.parse import urljoin

BaseUrl='http://test.com/html/a.html'
#print(">>",urljoin(BaseUrl,"b.html"))
#print(">>",urljoin(BaseUrl,"sub/bug.html"))
print(">>",urljoin(BaseUrl,"index.html"))
#print(">>",urljoin(BaseUrl,"../img/img.jpg"))
