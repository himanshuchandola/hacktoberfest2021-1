import requests, json
url = input("URL VIDEO: ")
r = requests.get("https://billal.herokuapp.com/api/igdown?url="+url)
j = json.loads(r.text)
print ("URL VIDEO: "+j["result"]["urlvid"])
