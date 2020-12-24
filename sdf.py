from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://data.ekape.or.kr/openapi-data/service/user/grade/confirm/cattle?serviceKey=A5oyjSJAhc93NY4ntIbQ53Y4Ni2wBVOgbBeG2ieNFGNZgvh0HvunpLiP39dsIEpV4QZaTqmHClG7lgCNlirWjg%3D%3D&issueNo=0505-180&issueDate=2013-01-10'

request = Request(url)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body
