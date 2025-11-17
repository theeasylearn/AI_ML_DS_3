html_doc = """
<html><head><title>the easylearn academy</title></head>
<body>
<p class="title"><b>AI ML DS </b></p>
<p class="title">any IT student can join</p>
<p class="story">
artificial intelligence machine learning and data science 
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
    <li>Item 5</li>
</ul>
</p>
<p class="summery">end of document</p>
</body>
</html>
"""
# from package-name import module name
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)
print(soup.title.text)
print(soup.p.text)
print(soup.ul.text)
print(soup.find('p',class_='summery').text)
#display each item 
for item in soup.find_all('li'):
    print(item.text)

#fetch all para with class title
for item in soup.find_all('p',class_='title'):
    print(item.text)