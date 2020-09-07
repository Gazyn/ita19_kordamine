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
    splitted = line.split("\t") #List kus elemendid on: Artist, Album, Aasta, Pealkiri
    if not splitted == ['']: #Faili lõpus on tühi rida
        laulud.append(Laul(splitted[3], splitted[0], splitted[2], splitted[1])) #Pealkiri, laulja, aasta, album
file.close()

for i in laulud:
    if i.album not in albumidOlemas: #Kui albumit pole juba lisatud albumite listi
        albumid.append(Album(i.album, i.aasta, i.laulja))
        albumidOlemas.append(i.album)
    for j in albumid: #Leia album kuhu laul kuulub
        if i.album == j.pealkiri:
            j.lisaLaul(i)

for i in albumid:
    if i.pealkiri not in lauljadOlemas: #Kui lauljat pole juba lisatud lauljate listi
        lauljad.append(Laulja(i.laulja))
        lauljadOlemas.append(i.laulja)
    for j in lauljad: #Leia laulja kuhu album kuulub
        if i.laulja == j.nimi:
            j.lisaAlbum(i) #Funktsioon lisab ka kõik albumi lood laulja lugude alla