# načtení souboru
with open ('CR_nepovedene.csv', encoding='utf-8') as vstup:
    radky = vstup.readlines()

# oddělení řádků
radek = [radek.split('\n') for radek in radky]
udaje = [udaj[0].split(';') for udaj in radek]

# vybrání adres a uložení do proměnné (pokud ulice neobsahuje žádný údaj, vyplní se název obce)
adresy = []
for udaj in udaje:
    ulice = udaj[6]
    cp = udaj[7]
    obec = udaj[9]
    if ulice == '':
        adresa = obec + ' ' + cp + ', ' + obec
    else:
        adresa = ulice + ' ' + cp + ', ' + obec
    adresy.append(adresa + '\n')

# uložení adres do souboru
with open('adresy_nepovedene_pro_gpsvizualizer.csv', mode='w', encoding='utf-8') as vystup:
     vystup.writelines(adresy)