import urllib.request, time, hashlib
baseurl = "http://superunicorn.mybluemix.net"
#baseurl = "http://127.0.0.1:8080"

appID = hashlib.sha224(str(time.time()).hexdigest()[-6:])

i = 0
while i < 10:
	urllib.request.urlopen(baseurl+"/alive?appID=" + appID)
	time.sleep(5)
	i+=1
