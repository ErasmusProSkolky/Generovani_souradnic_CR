# import modulu geopy
from geopy.geocoders import Nominatim
 
# načtení the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# otevření souboru
with open('seznam_MS_CR_final.csv', encoding='utf-8') as vstup:
    radky = vstup.readlines()

# vytvoření seznamu z jednoho řádku
jeden_radek = [radek.split('\n') for radek in radky]

# vyfiltrování pouze typ "Mateřské školy"
skolky = []
for cast_radku in jeden_radek[1:]:
    # rozdělení řádku na jednotlivé údaje
    cast = cast_radku[0].split(";")
    # vyfiltrování pouze MŠ
    if cast[5] == "Mateřská škola":
        skolky.append(cast_radku)

# proměnné pro ukládání 
nepovedene = []
povedene = []

# generování souřadnic - povedené se ukládají do jednoho souboru a nepovedené do jiného
for cast_radku in skolky:
    try:
        # rozdělení řádku na jednotlivé údaje
        cast = cast_radku[0].split(";")

        # načtení adresy
        ulice = cast[6]
        cp = cast[7]
        obec = cast[9]
        adresa = ulice + " " + cp + ", " + obec
        getLoc = loc.geocode(adresa)
        
        # vypsání adresy a souřadnic (pouze pro kontrolu, že se generují)
        print(getLoc.address)        
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)

        # uložení potřebných údajů do proměnné povedené      
        data = ""
        for casti in cast:
            data+=casti+";"   
        povedene.append(data + str(getLoc.latitude) + ";" + str(getLoc.longitude) + "\n")
    except Exception as chyba:
        # uložení potřebných údajů do proměnné nepovedené
        data_nepov = ""
        for casti in cast:
            data_nepov+=casti+";"    
        nepovedene.append(data_nepov+"\n")
        pass

# vložení hlavičky u povedených
hlavicka = "IZO"+ ";" + "KRAJ"+ ";" + "PLNY_NAZEV" + ";" + "NAZEV" + ";" + "WEB" + ";" + "TYP" + ";" + "ULICE" + ";" + "CISLO_POPISNE" + ";" + "PSC" + ";" + "MESTO" + ";" + "KAPACITA" + ";" + "OBSAZENOST" + ";" + "ZADOSTI_NEVYHOVENO_CELKEM" + ";" + "ZADOSTI_NEVYHOVENO_SPADOVE" + ";" + "ZADOSTI_VYHOVENO_CELKEM" + ";" + "ZADOSTI_VYHOVENO_SPADOVE" + ";" + "NASTOUPILY_CELKEM" + ";" + "NASTOUPILY_SPADOVE" + ";" + "LATITUDE" + ";" + "LONGITUDE" + "\n"
povedene.insert(0,hlavicka)
#print(povedene)

# uložení povedených do souboru
with open("CR_povedene_MS.csv", "w", encoding="utf-8") as vystup:
    vystup.writelines(povedene)

# uložení nepovedených do souboru
with open("CR_nepovedene.csv", "w", encoding="utf-8") as soubor:
    soubor.writelines(nepovedene)