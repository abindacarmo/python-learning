# iha ne'e ita koko halo while looping konaba hamosu numeru sira tuir saida mak ita sei input

print("=========Ezemplo primeiro==========")
i = 10
while i >= 0:
    print(i)
    inputt = input("Hili entre Sai ga Kontinua: ")
    if inputt == "sai":
        break
    elif inputt == "kontinua":
        i -= 1
    else:
        print("Input invalisu")


    
# Tuir mai ita sei halo menu ida hodi 
print("=======ezemplo segundo===============")

def fo_saimenu():
    print("==================")
    print("Menu")
    print("==================")
    print("1. Greeting name")
    print("2. sura kuadrado")
    print("3. cek par/impar")
    print("4. Sai")



while True:
    fo_saimenu()
    hili_opsaun = input("hili menu: ")

    if hili_opsaun == "1":
        input_naran = input("ita nia naran saida? : ")
        print("halooo ", input_naran)
    
    elif hili_opsaun == "2":
        input_numeru = int(input("input numeru: "))
        result = input_numeru * input_numeru
        print("kuadradu husi ", input_numeru ,"mak ", result)
    
    elif hili_opsaun == "3":
        input_numeru2 = int(input("input numeru: "))
        if input_numeru2 % 2 == 0:
            print(input_numeru2 ,"numeru par")
        else:
            print(input_numeru2 ,"numeru impar")
    elif hili_opsaun == "4":
        break

    else:
        print("opsaun la existe!")
    