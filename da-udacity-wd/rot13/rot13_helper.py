import logging

def converted_text(inputText):
	logging.debug("In main-{}".format(inputText))
	output = ""
	for c in inputText:
		output = output + (encode_rot13(c))
	return output

def encode_rot13(char):
	sub = 0
	if char.isalpha():
		logging.debug("In isalpha-{}".format(char))
		if char.islower():
			if ord(char) + 13 > 122:
				sub = 122 - ord(char)
				return chr(ord('a') - 1 + 13 - sub)
			else:
				return chr(ord(char) + 13)
		elif char.isupper():
			if ord(char) + 13 > 90:
				sub = 90 - ord(char)
				return chr(ord('A') - 1 + 13 - sub)
			else:
				return chr(ord(char) + 13)
	else:
		logging.debug("In ELSE-{}".format(char))
		return char