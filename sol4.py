import requests


base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

num = "82294"

url = base_url + num


def getnum(wst):
	i = len(wst) - 1
	enum = ""
	while True:
		if ord(wst[i]) >= ord("0") and ord(wst[i]) <= ord("9"):
			enum += wst[i]
			i-=1

		else:
			break

	num = enum[::-1]
	return num


print(num)

while True:
	r = requests.get(url)
	if r.status_code != 200:
		break
	wstr = r.text
	print(wstr)
	# print(wstr)
	num = getnum(wstr)
	url = base_url + num
	# print(url)
