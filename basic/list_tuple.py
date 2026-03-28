# Iha file ida ne'e ita sei aprende konaba LIST, DICTIONARY no TUPLES
# maibe iha file ida ne'e ita sei aprende deit list no tuple dictionary sei iha file foun ida

# tamba saida mak buat sira ne'e importante?
# durante ne ita rai dados hanesan tuir mai ne'e:
# numeru1 = 10
# numeru2 = 20
# numeru3 = 30
# ...

# exemplo karik dados ne'e too 1000 tidak mungkin ita mos halo variable hamutuk 1000 too?

# nahh husi ida ne'e hadir lahh list, dictionary no tuple hodi bele rai dados barak tuir ita nia hakarak iha variable ida nia laran.

# uuhh oinsa karik eehh.. mai ita haree hamutuk:

# definisaun

# LIST - konjunto dados ordenado, bele modifika
# TUPLE - konjunto husi dados ordenado, labele modifika
# DICTIONARY - konjunto dados ho label/naran


# LIST 

dados_aifuan = ["apple", "jambua", "haas"] # iha list ida ne'e iha dados ne'e barak iha variable ida nia laran no iha nia numeru index idak idak
#               index 0   index 1   index 2
print(dados_aifuan)

# ita bele foti husi bolu nia index idak idak:

print(dados_aifuan[0]) #nia output sei sai apple
print(dados_aifuan[2]) # nia output sei sai haas

# iha list mos ita bele modifika dados sira

# aumenta dados
dados_aifuan.append("saburaka")
print(dados_aifuan)

# troka dados
dados_aifuan[0] = "pateka"
print(dados_aifuan)

# hamoos dados
dados_aifuan.remove("haas")

print(dados_aifuan)


# TUPLES
# hanesan mos ho LIST maibe nia labele modifika

koordinat = (10, 20) # uza parentesis baibain

print(koordinat[0])
print(koordinat[1])

koordinat["0"] = 90 # error! tuple labele modifika

# bainhira mak ita uza tuple?
# dados ne'ebe labele modifika:
#     - koordinat GPS
#     - data moris
#     - kode kor RGB