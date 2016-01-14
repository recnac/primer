import urllib.request
baseurl = "http://superunicorn.mybluemix.net"
#baseurl = "http://127.0.0.1:8080"

for j in range(0,100): #100 prime numbers
	p = int(urllib.request.urlopen(baseurl+"/getjob").read())
	print("Checking number %s" % p)

	for i in range(2,p):
		if (p % i) == 0:
			urllib.request.urlopen(baseurl+"/noprime?number=%s" % p)
			break
	else:
		urllib.request.urlopen(baseurl+"/prime?number=%s" % p)
