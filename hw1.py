import requests
response = requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding="big5"
book1 = response.text
book1[:]
