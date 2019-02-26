import requests
from lxml import html

#storing response
response = requests.get('http://qsstechnosoft.com/')
#creating lxml tree from response body
tree = html.fromstring(response.text)

#Finding all anchor tags in response
hrefs = [item.get('href') for item in tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "owl-grab", " " ))]')]
print(hrefs)