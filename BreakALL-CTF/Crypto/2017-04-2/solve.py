encrypt = open("./encrypt", "rb").read()
decrypt = ""

print(type(encrypt))
print(type(decrypt))

encrypt = encrypt.decode("utf-8")

print(type(encrypt))
print(type(decrypt))

for i in range(0, len(encrypt) - 5, 5):
    decrypt = decrypt + encrypt[i + 4]

print(decrypt)
