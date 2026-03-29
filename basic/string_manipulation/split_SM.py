# split() iha string_manipulation mak hanesan oinsa ita bele fahe string
# ezemplo iha file CSV
# "Abinda,22,Dili,Timor-Leste"

# maibe ita preseza fahe tiha sai:
# naran "Abinda"
# tinan "22"
# Municipio "Dili"
# nasaun "Timor-leste"


data = "Abinda,22,Dili,Timor-Leste"
result = data.split(",")
print(result)

# fahe liu husi spasce
data2 = "Hau moris iha Dili"
print(data2.split(" "))   # → ["Hau", "moris", "iha", "Dili"]

# fahe liu husi strip(-)
data3 = "2026-03-29"
print(data3.split("-"))   # → ["2026", "03", "29"]


lina_csv = "Abinda,22,Dili,Timor-Leste"

data = lina_csv.split(",")

naran   = data[0]   # → "Abinda"
tinan   = data[1]   # → "22"
municipio   = data[2]   # → "Dili"
nasaun = data[3]   # → "Timor-Leste"

print(f"Naran: {naran}")
print(f"Tinan: {tinan}")
print(f"Kota : {municipio}")
print(f"Nasaun: {nasaun}")


print("====konjunto ho dictionary=====")

estudante = {
    "naran": data[0],
    "tinan": data[1],
    "municipio": data[2],
    "nasaun": data[3]
}

print(estudante)


print("====Treinu===")

dia = "2026-03-29"
dia_mos = dia.split("-")
print(dia_mos)

print("Tinan:", dia_mos[0])
print("Fulan:", dia_mos[1])
print("Loron:", dia_mos[2])

data_estudante = "Abinda,22,Dili,Timor-Leste"
data_estudante_mos = data_estudante.split(",")

estudante_dict = {
    "naran": data_estudante_mos[0],
    "tinan": data_estudante_mos[1],
    "municipio": data_estudante_mos[2],
    "nasaun": data_estudante_mos[3]
}

print(estudante_dict)

all_data = [
    "Abinda,22,Dili",
    "Dito,20,Baucau",
    "Maria,18,Suai"
]

# all_data_mos = all_data[0].split(",")
for i in all_data:
    dataa = i.split(",")
    narann = dataa[0]
    municipioo = dataa[2]

    print(narann, municipioo)

