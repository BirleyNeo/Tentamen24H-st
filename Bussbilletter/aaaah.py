import json
import datetime
import uuid

def loadJson(path):
    with open(path, "r") as file:
        return json.load(file)

##å kaste inn alle nye brukere
def dumpJson(dumpObj, path):
    with open(path, "w") as file:
        json.dump(dumpObj, file, indent=4)

brukere = loadJson("Bussbilletter/billetter.json")
busses = loadJson("Bussbilletter/busses.json")


#funksjon for bestilling
def bestill():
    bruker = {
        "fornavn": input("Skriv fornavnet ditt her: "),
        "etternavn": input("Skriv etternavnet ditt her: "),
        "antallPassasjerer": int(input("Skriv antall passasjerer: ")),
        "antallDagerLeie": int(input("Skriv antall dager bussen skal leies: ")),
        "totalDistanse": int(input("Skriv distanse av turen her i kilometer: ")),
        "valgtBuss": None,
        "totalpris": None,
        "turFullført": False,
        "datoForBestilling": datetime.datetime.now().strftime("%c")
    }

    valgtBuss = input("Velg en buss (skriv navnet): ").lower()
    for buss in busses:
        if valgtBuss == buss["bussNavn"].lower():
            if bruker["antallPassasjerer"] > buss["antallSeter"]:
                print(f"Bussen {buss['bussNavn']} har ikke nok seter. Bestillingen ble ikke fullført.")
                return

            bruker["valgtBuss"] = buss["bussNavn"]
            bruker["totalpris"] = int(buss["pris"]) * bruker["antallDagerLeie"] + 90 * bruker["totalDistanse"]

            for buss in busses:
                if(valgtBuss.lower() == buss["bussNavn"].lower()):
                    if(buss["ledig"] == False):
                        busses["bussID"] = buss["ID"]
                        for buss in busses:
                            if buss["bussNavn"] == valgtBuss:
                                buss["ledig"] = False
                                
            break
    else:
        print("Ugyldig bussvalg. Bestillingen ble ikke fullført.")
        return

    brukere.append(bruker)
    dumpJson(brukere, "Bussbilletter/billetter.json")
    print(f"Bestilling for {bruker['fornavn']} {bruker['etternavn']} er lagt til!")


#funksjon for å legge til busser
def leggeTilBuss():
    buss = {
        "bussNavn": input("skriv inn navn på bussen: "),
        "bussID": str(uuid.uuid4()),
        "antallSeter": input("skriv antall passasjerer: "),
        "ledig": True,
        "pris": input("prisen på bussen: "),
        }
    busses.append(buss)
    dumpJson(busses, "bussbestilling/busses.json")


#funksjon for list alle busser
def All_Busses():
    for buss in busses:
        print(buss["bussNavn"])
    
#funksjon til å list ut alle bestillingene
def All_Orders():
    for bruker in brukere:
        print(bruker["firstname"])
    for buss in busses:
        print(buss["bussNavn"])


#funksjon for å avslutte en busstur
def Fullføre_Bestilling():
    bussName = input("Navn på bestillingen: ")
    buss = None

    for cur_buss in brukere:
        if(bussName == cur_buss["navn"]):
            buss = cur_buss
            break

    if buss == None:
        print("Bussen finnes ikke")
        return

    count = 0
    for buss in brukere:
        print(count)
        if(buss["ID"] == buss["bussId"]):
            brukere.pop(count)
            dumpJson(brukere, "Bussbilletter/billetter.json")
            break
        count += 1    

    buss["bestillt"] = None
    dumpJson(brukere, "Bussbilletter/billetter.json")

#menu
def menu():
    print("----- User Menu -----")
    print("---------------------")
    print("1. Bestille en busstur")
    print("2. List ut alle bestillte bussturer")
    print("3. Fullføre eller slette en bestilling")
    print("4. Se alle Busser")
    print("0. Slutt programmet")
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