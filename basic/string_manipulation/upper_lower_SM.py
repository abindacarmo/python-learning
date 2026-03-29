# iha parte ida ne'e ita bele muda letra kiik ba boot no husi letra boot ba fali kiik

# ex: user login ho email:
# "ABINDA@gmail.com"
# "abinda@GMAIL.com"
# "Abinda@Gmail.Com"

# padahal email hanesan deit
# maibe programa senti ne ketak ketak

# exemplo primeiro

email = "ABINDA@Gmail.Com"

print(email.upper())  # → "ABINDA@GMAIL.COM"
print(email.lower())  # → "abinda@gmail.com"

# iha versaun 3 hodi muda letra

naran = "abinda carmo"

print(naran.upper())       # → "ABINDA CARMO"  letra hotu muda ba boot
print(naran.lower())       # → "abinda carmo"  letra hotu muda ba kiik
print(naran.capitalize())  # → "Abinda carmo"  muda letra primeiro deit mak ba boot
print(naran.title())       # → "Abinda Carmo"  kada liaguan muda ba letra boot


print("=======Exemplo segundo=======")
# ezemplo real halo validasaun email

email_database = "abindacarmo@gmail.com" # ne'ebe mak rai iha database

email_user = input("input ita nia email: ") # user input fali email "ABINDACARMo@Gmail.Com"

if email_user.lower() == email_database: # wainhira user input uza letra boot hotu entaun sei muda tiha ba letra kiik hotu
    print("login ho susesu!")

else:
    print("Email la bele accept!")