teks = input("Text : ").encode('utf-8')
pemisah = input("Separator : ")
bagiduo = [teks.hex()[i:i+2] for i in range(0, len(teks.hex()), 2)]
print("="*20+" \033[33mResult\033[39m "+"="*20)
print(pemisah+pemisah.join(bagiduo))
print("="*48)