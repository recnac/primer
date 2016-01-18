import urllib.request, time, random, string
baseurl = "http://superunicorn.mybluemix.net"
#baseurl = "http://127.0.0.1:8080"

appID = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))

while True:
	urllib.request.urlopen(baseurl+"/alive?appID=" + appID)
	time.sleep(5)
	
