# Simple Python Code
# Hex Encoder and Decoder with Separator (Example :'\x' , ' 0x' , ',0x' , 'h,')
# Code by Mugi F.
# github.com/mugi789
print(""" 
     __ __         
    |  |  |___ _ _ 
    |     | -_|_|_|
    |__|__|___|_|_|
     _____               _            ____                _         
    |   __|___ ___ ___ _| |___ ___   |    \ ___ ___ ___ _| |___ ___ 
    |   __|   |  _| . | . | -_|  _|  |  |  | -_|  _| . | . | -_|  _|
    |_____|_|_|___|___|___|___|_|    |____/|___|___|___|___|___|_|  
                                                                
    """)
def menu():
    print(" 1. Hex to Text")
    print(" 2. Text to Hex")
    print(" 3. Exit")
    pilih = int(input(" Select number : "))
    if pilih == 1:
        print("-"*20)
        from converter import hex2txt
    elif pilih == 2:
        print("-"*20)
        from converter import txt2hex
    elif pilih == 3:
        print("Bye")
        exit()
    else:
        print("="*20)
        print("\033[31m   Wrong input !!\033[39m")
        print("="*20)
        menu()
menu()
