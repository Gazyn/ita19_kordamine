import sqlite3

ühendus = sqlite3.connect('andmebaas.db')
c = ühendus.cursor()

c.execute("CREATE TABLE laulud (artist text, album text, aasta text, laul text)") #saaks teha eraldi faili et algselt luua, aga see oleks täpselt sama plus see üks rida.

for i in open("albumid.txt",mode="r",encoding="UTF-8"):
    info = i.strip().split("\t")
    for text in info:
        if "'" in text:
            info[info.index(text)] = text.replace("'", "''")
    c.execute("INSERT INTO laulud VALUES ('{}','{}','{}','{}')".format(info[0],info[1],info[2],info[3]))

ühendus.commit()

ühendus.close()