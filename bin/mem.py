import urllib.request, time
baseurl = "http://superunicorn.mybluemix.net"
#baseurl = "http://127.0.0.1:8080"

while True:
	urllib.request.urlopen(baseurl+"/alive")
	time.sleep(5)
