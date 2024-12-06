import json 
import datetime
import uuid

#å få oppdatere json filen
def loadJson(path):
    with open(path, "r") as file:
        return json.load(file)

#å kaste inn alle nye brukere
def dumpJson(dumpObj, path):
    with open(path, "w") as file:
        json.dump(dumpObj, file, indent=4)

brukere = loadJson("Bussbilletter/billetter.json")
busses = loadJson("Bussbilletter/busses.json")


#funksjon for bestilling
def bestill():
    try:
        bruker = {
            "fornavn": input("Skriv fornavnet ditt her: "),
            "etternavn": input("Skriv etternavnet ditt her: "),
            "antallPassasjerer": int(input("Skriv antall passasjerer: ")), #hvor mange folk skal gå i bussen
            "antallDagerLeie": int(input("Skriv antall dager bussen skal leies: ")), #hvor mange dager bussen kommer til å bli brukt
            "totalDistanse": int(input("Skriv distanse av turen her i kilometer: ")), #hvor langt bussen trenger å kjøre, til å finne prisen per km
            "valgtBuss": None, #bussen man kommer å velge ut (forskjellige seter, priser, ...)
            "totalpris": None, #prisen usern trenger å betale; regner ut km-prisen og prisen per dagen
            "turFullført": False, #om turen har blitt gjort eller ikke
            "datoForBestilling": datetime.datetime.now().strftime("%c") #når tid bestilling ble bestillt
        }
        valgtBuss = input("Velg en buss (skriv navnet): ").lower() #velge ut hvilken buss man vil ha ifra json fil listen
        for buss in busses:
            if valgtBuss == buss["bussNavn"].lower():
                if bruker["antallPassasjerer"] > buss["antallSeter"]:
                    print(f"Bussen {buss['bussNavn']} har ikke nok seter. Bestillingen ble ikke fullført.") #hvis det er for mange folk for bussen
                    return

                bruker["valgtBuss"] = buss["bussNavn"]
                bruker["totalpris"] = int(buss["pris"]) * bruker["antallDagerLeie"] + 90 * bruker["totalDistanse"] #utregning av total prisen
                if(buss["ledig"] == True): #sjekker om bussen er bestillt eller ikke
                    buss["ledig"] = False #sier at bussen har blitt bestillt
                elif(buss["ledig"] == False): #hva den må gjøre hvis bussen er ikke ledig
                    print("Bussen er ikke tilgjengelig! Prøv en annen buss.")
                    return
                break
            else:
                print("Ugyldig bussvalg. Bestillingen ble ikke fullført.")
                return
        
    #Når man ikke skriver inn rett, kommer denne feil koden
    except:
        print("Det oppstå en feil, prøv på nytt!")

    #Oppdater JSON-filene
    brukere.append(bruker)
    dumpJson(brukere, "Bussbilletter/billetter.json")
    dumpJson(busses, "Bussbilletter/busses.json")
    print(f"Bestilling for {bruker['fornavn']} {bruker['etternavn']} er lagt til!")


#funksjon for å legge til busser
def leggeTilBuss():
    buss = {
        "bussNavn": input("skriv inn navn på bussen: "), #navn
        "bussID": str(uuid.uuid4()), #id til bussen
        "antallSeter": input("skriv antall passasjerer: "), #sier hvor mange folk passer i en buss
        "ledig": True, #viser om man kan bruke bussen, eller om den er allerede bestillt
        "pris": input("prisen på bussen: "), #bussprisen per døgn
        }
    #Oppdater JSON-filene
    busses.append(buss)
    dumpJson(busses, "Bussbilletter/busses.json")


#funksjon for list alle busser
def All_Busses():
    for buss in busses:
        print(buss["bussNavn"])
    
#funksjon til å list ut alle bestillingene
def All_Orders():
    for bruker in brukere:
        print(bruker["valgtBuss"])


#funksjon for å avslutte en busstur og slette bestillingen
def Fullføre_Bestilling():
    bussNavn = input("Navn på bussen: ").lower()
    bussFunnet = False

    #Oppdater bussens status til ledig
    for buss in busses:
        if buss["bussNavn"].lower() == bussNavn and buss["ledig"] == False:
            bussFunnet = True
            buss["ledig"] = True
            print(f"Bussen '{buss['bussNavn']}' er nå satt som ledig.")
            break

    if not bussFunnet:
        print("Ingen buss med det navnet ble funnet i systemet.")
        return

    #Fjern tilknyttet bestilling
    bestillingFunnet = False
    for bruker in brukere[:]:  #Lager en kopi av listen for sikker sletting
        if bruker["valgtBuss"].lower() == bussNavn:
            brukere.remove(bruker)
            bestillingFunnet = True
            print(f"Bestillingen for {bruker['fornavn']} {bruker['etternavn']} er fullført/slettet.")
            break

    if not bestillingFunnet:
        print("Ingen bestillinger ble funnet for denne bussen.")

    #Oppdater JSON-filene
    dumpJson(brukere, "Bussbilletter/billetter.json")
    dumpJson(busses, "Bussbilletter/busses.json")

#funksjon til å bestemme mellomrom
def mellomrom(num):
    for x in range(num):
        print("")

#menu
def menu():
    mellomrom(2)
    print("----- User Menu -----")
    mellomrom(1)
    print("1. Bestille en busstur")
    print("2. List ut alle bestillte bussturer")
    print("3. Fullføre eller slette en bestilling")
    print("4. Se alle Busser")
    print("0. Slutt programmet")
    mellomrom(1)
    valg = input("velg noe ifra menyen: ")
    return valg


#main
def main():
    run = True
    while run:
        mittvalg = menu()
        if (mittvalg == "1"):
            bestill()
        elif (mittvalg == "2"):
            All_Orders()
        elif (mittvalg == "3"):
            Fullføre_Bestilling()
        elif (mittvalg == "4"):
            All_Busses()
        elif (mittvalg == "0"):
            run = False
        else:
            print("ugyldig valg!")

main()