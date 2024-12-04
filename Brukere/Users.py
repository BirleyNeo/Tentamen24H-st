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
users = loadJson("Repetisjon/users.json")

#lag ny bruker
def Add_user():
    user = {
        "firstname": input("skriv inn fornavn: "), #fornavn
        "lastname": input("skriv inn etternavn: "), #etternavn
        "telefonnr": input("skriv inn telefon nummeret: "), #telefon nr
        "address": input("skriv inn adressen: "), #adressen
        "epost": input("skriv inn epost: "), #epost
        "LagtTil": datetime.datetime.now().strftime("%c") #dato og klokkeslettet
    }
    #lagre brukere
    users.append(user)
    dumpJson(users, "Brukere/lagring.json") 
    print(user["firstname"] + " er lagt til som en ny user!")

#list ut alle brukere med fornavnet
def All_users():
    for user in users:
        print(user["firstname"])

#menu/å velge ut hvilken funksjon kommer til å bli kjørt
def menu():
    print("----- User Menu -----")
    print("---------------------")
    print("1. legg til ny user")
    print("2. list ut alle brukere")
    print("0. slutt programmet")
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
        elif (mittvalg == "0"):
            run = False
        else:
            print("ugyldig valg!")

main()