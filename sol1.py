def decode(code):
	n = len(code)
	decode = ""
	for i in range(n):
		if code[i] == " " or code[i] == "." or code[i] == "(" or code[i] == ")" or code[i]=="'":
			continue

		asc = ord(code[i])
		asc += 2
		if asc > 122:
			asc = 96 + asc - 122

		char = chr(asc)
		decode = decode + char

	print(decode)


# decode("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")


decode("map")