import os, time, urllib.request
id = str(time.time())
while True:
	try:
		urllib.request.urlopen('http://packify.mybluemix.net/notify?'+id)
	except:
		print("error")
	time.sleep(2)
