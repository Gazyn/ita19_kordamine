from laul import Laul
from album import Album
from laulja import Laulja

laulud = []
albumid = []
lauljad = []

albumidOlemas = []
lauljadOlemas = []

file = open("albumid.txt", mode="r")
for i in file:
    line = i.strip() # Salvestab rea
    splitted = line.split("\t") #List kus elemendid on: Artist, Album, Aasta, Nimi
    if not splitted == ['']: #Faili lõpus on tühi rida
        laulud.append(Laul(splitted[3], splitted[0], int(splitted[2]), splitted[1])) #Nimi, laulja, aasta, album
file.close()

for i in laulud:
    if i.album not in albumidOlemas: #Kui albumit pole juba lisatud albumite listi
        albumid.append(Album(i.album, int(i.aasta), i.laulja))
        albumidOlemas.append(i.album)
    for j in albumid: #Leia album kuhu laul kuulub
        if i.album == j.nimi:
            j.lisaLaul(i)

for i in albumid:
    if i.laulja not in lauljadOlemas: #Kui lauljat pole juba lisatud lauljate listi
        lauljad.append(Laulja(i.laulja))
        lauljadOlemas.append(i.laulja)
    for j in lauljad: #Leia laulja kuhu album kuulub
        if i.laulja == j.nimi:
            j.lisaAlbum(i) #Funktsioon lisab ka kõik albumi lood laulja lugude alla

doing = int(input("Valige mida soovite teha, 1-4: "))
"""
1 - väljastada kõik sisu failist, et iga album oleks teistes näiteks kriipsude jadaga eraldatud (-------)
2 - otsida failist albumid pealkirja järgi või aasta numbri järgi - tulemusena väljastatakse nimekiri leitud albumitest
3 - otsida failist laulud nime järgi - tulemusena väljastatakse, mis albumis antud laul on ja kes on laulja ning mis aasta album see on
4 - otsida failist lauljad - tulemusena väljastatakse antud laulja albumite pealkirjad ja aastad
"""
tulemused = [] #miks ei või pythonis olla switch funktsioon?
if doing == 1:
    print("Väljastan kõik sisu failist")
    for i in laulud:
        tulemused.append(i)
if doing == 2:
    print("Otsin albumeid pealkirja või aasta numbri järgi")
    otsing = input("Sisesta otsing: ")
    for i in albumid:
        if otsing.lower() in i.nimi.lower() or otsing == i.aasta:
            tulemused.append(i)
if doing == 3:
    print("Otsin failist laulud nime järgi")
    otsing = input("Sisesta otsing: ")
    for i in laulud:
        if otsing.lower() in i.nimi.lower():
            tulemused.append(i)
if doing == 4:
    print("Otsin failist lauljad, väljastan albumid")
    otsing = input("Sisesta otsing: ")
    for i in lauljad:
        if otsing.lower() in i.nimi.lower():
            for album in i.albumid:
                tulemused.append(album)

print("-----Tulemused-----") #(üritab) universaalselt väljastada kõik andmed tulemuste kohta, olgu need laulud, albumid või artistid.
for i in tulemused:
    tekst = type(i).__name__ +" - " #Alustab igat rida tulemuse tüübiga - Laul, Album, Laulja
    for value in vars(i):
        tekst += str(value) #lisab väärtuse nime
        tekst += ": "
        if type(getattr(i, value)) is list: #albumi laulude või laulja albumite puhul väljastab nimesid, mitte objekte
            for element in getattr(i, value):
                tekst += element.nimi
                tekst += " "
        else:
            tekst += str(getattr(i, value)) #lisab väärtuse
        tekst += " | "
    print(tekst)
#Artiste ei väljastatagi kunagi, aga funktsionaalsus selleks on olemas.