# -*- coding: UTF-8

salattava = u'HEI, TÄTÄ EI PYSTYKÄÄN ENÄÄ MURTAMAAN KOVIN HELPOSTI.\n\
OIKEASTI TÄMÄ EI OLE TURVALLINEN SALAUS.'

aakkoset = u'ABCDEFGHIJKLMNOPQRSTUVXYZÄÖ'
avain = u'SALAISUUS'

i = 0
print("alkuperäinen:")
print(salattava)
print("--------------")
salattu = ""
for m in salattava: # Käy läpi merkit yksi kerrallaan
  monesko = aakkoset.find(m)
  if (monesko == -1): # Jos erikoismerkki
    salattu = salattu + m # ota sellaisenaan
  else: #muussa tapauksessa (tavallinen kirjain)
    # ota merkki joka on aakkosissa avaimesta valitun merkin (kohdasta i) osoittaman verran oikealle aakkosissa salattavasta merkistä
    # jos aakkoset loppuvat kesken, aloita alusta uudelleen
    salattu = salattu + aakkoset[(monesko + aakkoset.find(avain[i])) % len(aakkoset)]
  i = (i + 1) % len(avain) # ota avaimesta seuraava merkki seuraavaksi salausmerkiksi

print("salattu:")
print(salattu)
print("-----------")

# purkaminen
i = 0
purettu = ""
for m in salattu: # Käy läpi merkit yksi kerrallaan
  monesko = aakkoset.find(m)
  if (monesko == -1): # Jos erikoismerkki
    purettu = purettu + m # ota sellaisenaan
  else: #muussa tapauksessa (tavallinen kirjain)
    # ota merkki joka on aakkosissa avaimesta valitun merkin (kohdasta i) osoittaman verran 
    # vasemmalle aakkosissa salattavasta merkistä
    # jos aakkoset loppuvat kesken, aloita lopusta taaksepäin
    purettu = purettu + aakkoset[(monesko - aakkoset.find(avain[i])) % len(aakkoset)]
  i = (i + 1) % len(avain)


print("purettu:")
print(purettu)

