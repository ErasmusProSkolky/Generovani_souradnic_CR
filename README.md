Generování souřadnic + filtr pouze na MŠ
    
    soubor: souradnice_skolky_CR.py
    
    vstup: seznam_MS_CR.csv
    
    výstup: CR_povedene_MS.csv, 
            CR_nepovedene.csv

Extrakce adres z nepovedených
    
    soubor: pouze_adresy_nepovedene.py
    
    vstup: CR_nepovedene.csv
    
    výstup: adresy_nepovedene_pro_gpsvizualizer.csv
		
Extrakce souřadnic ze soubou vygenerovaného Gpsvizualizer, uložení souřadnic do jednotlivých řádků v CR_nepovedene.csv a následné uložení původně nepovedených adres do  CR_povedene_MS.csv
    
    soubor: uprava_nepovedene_adresy.py
    
    vstup: adresy_z_gpsvizualizer.csv, CR_nepovedene.csv
    
    výstup: CR_povedene_MS.csv - obohacený o nové řádky
