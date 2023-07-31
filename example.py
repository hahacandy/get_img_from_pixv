import requests
import shutil

# https://curlconverter.com/python/
# You can visit the link above to get the url, headers

url = ""
headers = {}

r = requests.get(
    url,
    headers=headers,
    allow_redirects=True
)

open('result.png', 'wb').write(r.content)