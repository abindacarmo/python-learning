# join ne vise versa ho split

# exemplo

# .split(",") → fahe string sai hanesan list ida
# .join(",")  → halo list ida sai string ida

data = ["Abinda", "22", "jomblo"]

data_join = ",".join(data)

print(data_join)


# bele uza spliting saida deit
liafuan = ["Hau", "moris", "iha", "Dili"]

print(" ".join(liafuan))    # → "Hau moris iha Dili"
print(",".join(liafuan))    # → "Hau,moris,iha,Dili"
print("-".join(liafuan))    # → "Hau-moris-iha-Dili"
print("".join(liafuan))     # → "HaumorisihaDili"


# ⚠️ importante

# join() so bele halo konjunto list ne'ebe content husi string deit labele iha integer karik iha integer entaun tenki/obrigatorio muda ba str(int)

# ✅ ne bele
data = ["Abinda", "Dili", "Timor"]
print(",".join(data))

# ❌ ne error! iha numeru integer
# data = ["Abinda", 22, "Dili"]
# print(",".join(data))  # → TypeError!

# ✅ solusaun → muda ba string
data = ["Abinda", str(22), "Dili"]
print(",".join(data))  # → "Abinda,22,Dili" ✅


mahasiswa = {
    "naran" : "Abinda",
    "tinan" : "22",
    "kota"  : "Dili"
}

# halo konjunto hamutuk sai lina csv ida
baris_csv = ",".join(mahasiswa.values()) #ita uza values para fo sai deit nia values tamba iha ne'eba ita uza dictionary
print(baris_csv)
# → "Abinda,22,Dili" ✅ bele ona rai iha file .csv



# troka spliting husi virgula ba fali iha space
dados = "Abinda,22,Jomblo"

list_dados = dados.split(",")
result = "-".join(list_dados)

print(result)


# Treinu
# level 1

liafuann = ["hau","hadomi", "Timor-Leste"]

liafuan_space = " ".join(liafuann)
print(liafuan_space)

# level 2
dadoss = ["Abinda", "22", "Dili", "Timor-leste"]
dados_csv = ",".join(dadoss)
print(dados_csv)

# level 3
# muda spliting husi virgula ba " | "
data_csv = "Abinda,22,Dili,Timor-Leste"
data_csv_split = data_csv.split(",") #primeiro ita muda uluk lai ba iha split pois mak ita uza fali ba join
data_csv_join = " | ".join(data_csv_split)

print(data_csv_join)

