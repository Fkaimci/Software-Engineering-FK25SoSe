def erstelle_experimente(first_experiment_id: int):

    try:

        first_experiment_id = int(first_experiment_id)  # zum Sicherstellen dass es eine ganze Zahl ist

    except ValueError:

        print("Fehler: Die ID muss eine ganze Zahl sein!")

        return []  # Falls Fehler, leere Liste zurückgeben

   

    experimente = []  

    heute = date.today().strftime("%Y-%m-%d")  # Aktuelles Datum als String speichern

   

    for i in range(10):  

        experiment = {

            "Id_Nummer": first_experiment_id + i,  

            "Versuchsleiter": "Ich",  # Immer der gleiche Leiter(Ich)

            "Erstellungsdatum": heute  # Gleiches Datum für alle

        }

        experimente.append(experiment)  # Experiment zur Liste hinzufügen

   

    return experimente  # Liste zurückgeben

 

def zeige_experimente(experimente: list):

    for i in range(5):  # zeigt nur die ersten 5 Experimente

        print(experimente[i])

 

def count_even_ids(experimente: list):

    gerade_anzahl = 0  # Zähler für gerade IDs

    for experiment in experimente:

        if experiment["Id_Nummer"] % 2 == 0:  # Prüfen, ob Zahl gerade ist

            gerade_anzahl += 1  

    return gerade_anzahl  


 

first_experiment_id = input("Geben Sie die erste ID ein: ")  

experimente = erstelle_experimente(first_experiment_id)  

 

if experimente:  # Falls die Liste nicht leer ist

    zeige_experimente(experimente)  

    print("Anzahl der Experimente mit gerader ID:", count_even_ids(experimente))
