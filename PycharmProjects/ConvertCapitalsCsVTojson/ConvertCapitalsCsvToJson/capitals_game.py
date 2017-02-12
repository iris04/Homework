import random
# Zufall importieren

capitals = {}
capitals["Oesterreich"] = "Wien"
capitals["Italien"] = "Rom"
capitals["Schweden"] = "Stockholm"
capitals["Finnland"] = "Helsinki"
capitals["Ungarn"] = "Budapest"
capitals["Tschechien"] = "Prag"

Punkte = 0 #Punkte starten mit 0

n_fragen = 4

for i in range(n_fragen):
    land = random.choice(capitals.keys())
    antwort = raw_input("Was ist die Hauptstadt von %s?" %land)
    if antwort.lower() == capitals[land].lower():
        Punkte += 1
    del capitals[land]

print "Du hast %i von %i Punkten erreicht!" %(Punkte, n_fragen)


