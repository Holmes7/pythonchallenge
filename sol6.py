import zipfile


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


num = "90052"
with zipfile.ZipFile('assets/channel.zip', 'r') as my_zip:
	while True:
		filename = "assets/channel/" + num
		if num == "":
			break

		print(my_zip.getinfo(num + ".txt").comment.decode(), end="")
		with open(filename + ".txt", "r") as f:
			all_lines = f.readlines()
			# print(all_lines)
		num = getnum(all_lines[0])


# with zipfile.ZipFile('assets/channel.zip', 'r') as my_zip:
# 	print(my_zip.comment.decode())
# 	for info in my_zip.infolist():
# 		comments.append(info.comment.decode())
