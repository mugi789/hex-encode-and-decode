hex = input("Input Hex with Separator : ")
bagiduo = [hex[i:i+2] for i in range(0, len(hex), 2)]
print("="*20+" \033[33mResult\033[39m "+"="*20)
try:
    print(bytes.fromhex(''.join(''.join(bagiduo).split(bagiduo[0]))).decode('ASCII'))
    print("="*48)
except:
    print("\033[31m it's not hex\033[39m")
    print("="*48)