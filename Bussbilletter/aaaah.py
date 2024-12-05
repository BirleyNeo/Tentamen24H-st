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
        "firstname": input("skriv inn fornavn: "), #fornavn
        "lastname": input("skriv inn etternavn: "), #etternavn
        "antallPassasjere": int(input("skriv inn antall passasjerer: ")), #Passasjerer
        "antallDager": int(input("skriv inn antall dager bussen kommer til å bli brukt: ")), #dagesgebyr
        "KmPris": int(input("hvor langt skal bussen kjøre? skriv i km: ")), #km gebyr
        "BestillingsDato": datetime.datetime.now().strftime("%c"), #dato og klokkeslettet
        "ValgtBuss": None,
        "FullførtBestilling": False,
        "TotalPris": None,
    }

    valgtBuss = input("Velg en buss (skriv navnet): ").lower()
    for buss in busses:
        if valgtBuss == buss["bussNavn"].lower():
            if bruker["antallPassasjere"] > buss["antallSeter"]:
                print(f"Bussen {buss['bussNavn']} har ikke nok seter. Bestillingen ble ikke fullført.")
                return

            bruker["valgtBuss"] = buss["bussNavn"]
            bruker["KmPris"] = int(buss["pris"]) * bruker["antallDager"] + 90 * bruker["KmPris"]
            break
    else:
        print("Ugyldig bussvalg. Bestillingen ble ikke fullført.")
        return

    brukere.append(bruker)
    dumpJson(brukere, "Bussbilletter/billetter.json")
    print(f"Bestilling for {bruker['firstname']} {bruker['lastname']} er lagt til!")


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


#funksjon for list ut bestillingene
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
            pass
        elif (mittvalg == "3"):
            Fullføre_Bestilling()
        elif (mittvalg == "0"):
            run = False
        else:
            print("ugyldig valg!")

main()