# -*- coding: UTF-8

salattava= u'HEI, KAIKKI ON HELPPOA KUN SEN OSAA!\n\
HARJOITUS TEKEE MESTARIN JA TYVESTÄ PUUHUN NOUSTAAN JA\n\
VOIMME LUETELLA MYÖS MUITA KULUNEITA LATTEUKSIA.\n\
MUTTA KOKEILLAANKO JOTAIN VÄHÄN VAIKEAMPAA?\n\
MITÄ PITEMPI TEKSTI, SITÄ HELPOMPI ON RATKAISTA\n\
SALAINEN AVAIN.'

print(salattava) # Tulostetaan salattava teksti

aakkoset = u'ABCDEFGHIJKLMNOPQRSTUVXYZÄÖ'
salaus = 10

s = "" 
for m in salattava: # Käydään salattava teksti läpi merkki kerrallaan
    monesko = aakkoset.find(m) # monesko kirjain aakkosissa merkki on?
    if (monesko == -1): # ei löytynyt (piste tai muu erikoismerkki?)
      s = s + m # lisätään s muuttujaan erikoismerkki ilman salausta
    else:
      # muussa tapauksessa (eli tavallinen aakkosten kirjain)
      # lisätään s muuttujaan merkki kohdasta (monesko + salaus). 
      # Jos merkit loppuvat, aloitetaan laskeminen alusta
      s = s + aakkoset[(monesko + salaus) % len(aakkoset)] 

print(s) # Tulostetaan kaikki s muuttujan merkit

