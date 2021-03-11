import sys

if len(sys.argv) != 2:
	print("usage: python caesar.py [k]\n\n k is an integer non-negative")
	sys.exit(1)

text = input("plaintext:  ")
output = "";
for i, c in enumerate(text, start=0):
	output += str(c) if (not text[i].isalpha()) else chr(ord(c) + int(sys.argv[1])%26)
		
print("ciphertext: " + output)