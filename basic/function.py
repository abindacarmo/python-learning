#FUNCTION

# function ne hanesan konjunto husi kode barak ne'ebe mak ita bele bolu dala barak
# exemplo function
# string
def greeting(name): # iha ne'e ita halo function ida ho naran greeting no iha parameter ida mak name
    print("halo", name) # ita hakarak ezekuta no name ne'e husi parameter name


greeting("Binda") # bolu function primeiro ho argument "Binda"
greeting("Ana") # bolu function segundo ho argument "Ana"


# ezemplo segundo
# somatorio
print("====WITH RETURN====")
def mais(a, b): # halo function ho parameter rua
    return a + b # tamba saida mak ita la uza print iha nee?, tamba ita hakarak atu rai nia total ne iha variable ida entaun ita tenke uza return
# kuandu ita uza print wainhira ita tau iha variable ida nia laran no halo nia result ne'e sai value nia sei fo sai none deit


result = mais(2, 5) # result sei sai 7 no nia sei sai value ida husi variable result

print("Resultado: ", result) # variable result ne'e sei uza fali iha kode sira seluk

# exemplo ita uza print
print("====WITH PRINT====")
def maiss(a, b):
    print (a + b)

maiss(2, 6) # nia sei fo sai los deit 8 no labele utiliza fali ba kode sira seluk tamba la iha varible ida hodi rai nia

result = maiss(2, 5) # nia so fo sai deit iha layar result 7 meibe labele sai value ba variable ida
print("Resultado: ", result) # wainhira ita execute kode ida ne'e nia sei sai NONE

# ita mos bele aumenta operasaunn seluk hanesan menus(-), vezes(*) no dividir(/), uza kode ida WITH RETURN ne.