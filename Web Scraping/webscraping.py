from email import header
import requests

url = 'https://httpbin.org/headers'

headers = {
   "john": "Chrome",

}
response = requests.get(url, headers=headers)
print(response.text)