# -*- coding: UTF-8
stringx = u'ABCDEFGHIJKLMNOPQRSTUVXYZÄÖ'
i = 0
# print(stringx)
for m in stringx: # Käy läpi merkit yksi kerrallaan
  s = ""
  for j in range(0, len(stringx)): # j käy läpi arvot 0 ... merkkien lukumäärä
    # lisätään muuttujaan s merkki kohdasta j+i. 
    # Jos j+i on isompi kuin merkkien määrä, jatketaan laskemista alusta 
    s = s + stringx[(j + i) % len(stringx)] + ","   

  print(s[:-1]) # Tulostetaan s ilman sen viimeistä merkkiä (joka olisi pilkku)
  i = i + 1 # i valitsee aloituskohdaksi seuraavalle riville seuraavan merkin

