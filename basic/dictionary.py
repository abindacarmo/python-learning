# exemplo hanesan kadernu konta no ita uza key-value


estudante = {
    "naran": "Abinda",
    "tinan": 22,
    "hela-fatin": "hera"
}
# iha ne'e key mak naran, tinan no hela-fatin no value mak Abinda, 22 no hera

# ita bele:

# foti dados liu husi nia label/key
print(estudante["naran"])
print(estudante["tinan"])

# ita bele aumenta

estudante["IPC"] = 3.43

print(estudante)

# ita bele muda
estudante["tinan"] = 23

print(estudante)

# ita bele hamoos dados
del estudante["hela-fatin"]
print(estudante)

# komparasaun entre sira nain3
# LIST → uza []
# aifuan = ["apel", "haas", "derok"]

# # TUPLE → uza ()
# kor = (255, 128, 0)

# # DICTIONARY → uza {}
# ema = {"naran": "Abinda", "tinan": 20}

#                 List        Tuple       Dictionary
# Simbol           []          ()             {}
# Bisa diubah?     ✅          ❌             ✅
# Akses data      index [0]   index [0]       key ["nama"]
# Urutan           ✅          ✅             ❌