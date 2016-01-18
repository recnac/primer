import urllib.request, time
baseurl = "http://superunicorn.mybluemix.net"
#baseurl = "http://127.0.0.1:8080"

appID = str(time.time())

while True:
	urllib.request.urlopen(baseurl+"/alive?appID=" + appID)
	time.sleep(5)
