import sys

if len(sys.argv) != 2:
	print("usage: python caesar.py [k]\n\n k is an integer non-negative")
	sys.exit(1)

text = input("plaintext:  ")
output = "";
for i, c in enumerate(text, start=0):
	aux = ord(c) + int(sys.argv[1])%26
	if aux > 122:
		aux = 96 + aux -122
	elif aux > 90 and aux < 97:
		aux = 64 + aux - 90
	output += str(c) if (not text[i].isalpha()) else chr(aux)
		
print("ciphertext: " + output)
