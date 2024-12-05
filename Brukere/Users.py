#importering av de forskjellige ting jeg trenger å bruke i programmet
import json
import datetime

#program å lagre brukere i json fil
##å få muligheten å lese json filen
def loadJson(path):
    with open(path, "r") as file:
        return json.load(file)

##å kaste inn alle nye brukere
def dumpJson(dumpObj, path):
    with open(path, "w") as file:
        json.dump(dumpObj, file, indent=4)

#det sier hvilken json fil vi skal lagre hva i
users = loadJson("Brukere/lagring.json")
busser = loadJson("Bussbilletter/billetter.json")

#lag ny bruker
def Add_user():
    user = {
        "firstname": input("skriv inn fornavn: "), #fornavn
        "lastname": input("skriv inn etternavn: "), #etternavn
        "epost": input("skriv inn epost: "), #epost
        "kontoDato": datetime.datetime.now().strftime("%c"), #dato og klokkeslettet
    }
    #lagre brukere
    users.append(user)
    dumpJson(users, "Brukere/lagring.json") 
    print(user["firstname"] + " er lagt inn!")

#funksjon til å bestille en buss
##sjekk antall passasjerer
###over 7, 15, 23
###gebyr
##liste av busser
def bus():
    buss = {
        "firstname": input("skriv inn fornavn: "), #fornavn
        "lastname": input("skriv inn etternavn: "), #etternavn
        "antallPassasjere": input("skriv inn antall passasjerer: "), #Passasjerer
        "dager": input("skriv inn antall dager bussen kommer til å bli brukt: "), #dagesgebyr
        "KmPris": input("hvor langt skal bussen kjøre? skriv i km: "), #km gebyr
        "BestillingsDato": datetime.datetime.now().strftime("%c"), #dato og klokkeslettet
        "TildeltBuss": None,
        "FullførtBestilling": False,
    }
    busser.append(buss)
    dumpJson(buss, "Bussbilletter/billetter.json") 
    print("Du har lagt inn en bestilling!")

#List ut bestillte bussturer
def All_busser():
    for buss in busser:
        if buss == False:
            print(buss)
        else:
            print("Det er ingen bestillte busser!")
#Fjerne eller fullføre en registrert bestilling
def Fullføre_Bestilling():
    bussName = input("Navn på bestillingen: ")
    buss = None

    for cur_buss in busser:
        if(bussName == cur_buss["navn"]):
            buss = cur_buss
            break

    if buss == None:
        print("Bussen finnes ikke")
        return

    count = 0
    for buss in busser:
        print(count)
        if(buss["ID"] == buss["bussId"]):
            busser.pop(count)
            dumpJson(busser, "Bussbilletter/billetter.json")
            break
        count += 1    

    buss["bestillt"] = None
    dumpJson(busser, "Bussbilletter/billetter.json")

#list ut alle brukere med fornavnet
def All_users():
    for user in users:
        print(user["firstname"])

#menu/å velge ut hvilken funksjon kommer til å bli kjørt
def menu():
    print("----- User Menu -----")
    print("---------------------")
    print("1. Legg til users")
    print("2. List ut alle brukere")
    print("3. Bestille en busstur")
    print("4. List ut alle bestillte bussturer")
    print("5. Fullføre eller slette en bestilling")
    print("0. Slutt programmet")
    valg = input("velg noe ifra menyen: ")
    return valg

#main programmet som sier hvilken tall ifra menyen tilhører til hvilken funksjon
def main():
    run = True
    while run:
        mittvalg = menu()
        if (mittvalg == "1"):
            Add_user()
        elif (mittvalg == "2"):
            All_users()
        elif (mittvalg == "3"):
            pass
        elif (mittvalg == "4"):
            pass
        elif (mittvalg == "5"):
            Fullføre_Bestilling()
        elif (mittvalg == "0"):
            run = False
        else:
            print("ugyldig valg!")

main()