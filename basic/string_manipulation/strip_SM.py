#  saida mak string manipulation?
# jere no hamoos teks atu nune'e bele utiliza ho loos husi ita nia programa.

# nia operasaun sira ne'ebe mak ita uza mak:
# .strip() hodi hamoos space
# .upper(), .lower() - troka letra sira ba letra boot ou kiik
# .split() - hodi fahe tiha String
# "".join() - halo konjunto entre string
# .replace() - troka liafuan
# .len() - hodi sura string nia naruk
# .find() - buka poszisaun liafuan nian
# f-string 
# .count() 

print("====ezemplo strip====")
# hamoos space
# strip ita uza wainhira user sira input sira nia naran la sengaja
#  aumenta fali space ita bele utiliza strip hodi hamoos space no 
# input mos bele tuir ita nia hakarak

naran = " Abinda "

print("-",naran,"-") # ho space
print("-",naran.strip(),"-") # laho space

# iha versaun 3
print(naran.strip())   # → "Abinda"      hamoos husi left & right
print(naran.lstrip())  # → "Abinda   "  hamoos left deit
print(naran.rstrip())  # → "Abinda   "  hamoos right deit

# exemplo real

naran = input("input ita nia naran: ")

# ita tenke uza varaible hodi rai fali naran ne'ebe sprit ona
naran_mos = naran.strip() # so hamoss deit space ne'ebe iha left no right laos iha klaran, maibe karik ita hakarak hamoos kalara ita uza fali .replace(" ", "")
print("haloo", naran_mos)
