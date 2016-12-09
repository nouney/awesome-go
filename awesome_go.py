import urllib.request
import re
import json
import sys

url = "https://raw.githubusercontent.com/avelino/awesome-go/master/README.md"
response = urllib.request.urlopen(url)
lines = response.readlines()

reg = re.compile(r"^\s*\* \[[^]]+\]\(https?:(?:www)?\/\/([^)]+)\)")

print("""
### Extended Awesome Go

*Daily clone of [avelino/awesome-go](https://github.com/avelino/awesome-go) with information from [Go-Search](http://go-search.org).*

:arrow_down: - Number of packages that imports this package

:star:  - Number of stars

---
""")
for line in lines:
    line = line.decode('utf-8').rstrip()
    m = reg.match(line)
    if m is not None:
        try:
            gos = urllib.request.urlopen("http://go-search.org/api?action=package&id={}".format(m.group(1)))
            data = json.loads(gos.read().decode('utf-8'))
            imported = len(data['Imported']) if data['Imported'] is not None else 0
            print("{} - :arrow_down:{} - :star:{}".format(line, imported, data['StarCount']))
        except:
            print(line)

    else:
        print(line)
