import os

myteam = [
         {
            "firstname": "Khabib", 
          "lastname": "Nurmagomedov",
          "Country": "Russia",
          "Age": 33,
          "Height": 5.10,
          "Career": "UFC",
          "RecordWins": 29,
          "Recordloss": 0,
          "RecordDraw": 0,         
         },

         {
            "firstname": "Alistair",
         "lastname": "Overeem",
         "Country": "Netherlands",
         "Age": 43,
         "Height": 6.5,
         "Career": "UFC",
         "RecordWins": 47,
         "Recordloss": 19,
         "Recorddraw": 0
         } ]







enemyteam = [
            {"firstname": "Brock", 
            "lastname": "Lesnar",
            "Country": "USA",
            "Age": 45,
            "Height": 6.3,
            "Career": "UFC",
            "RecordWins": 5,
            "Recordloss": 3,
            "RecordDraw": 0,      
               },
               { "firstname": "Jon", 
            "lastname": "Jones",
            "Country": "USA",
            "Age": 45,
            "Height": 6.3,
            "Career": "UFC",
            "RecordWins": 31,
            "Recordloss": 0,
            "RecordDraw": 0,   
               }

]



for key in myteam:
   print(f"{key}: {myteam[key]}")

#user_choice = input("Which fightet do you prefer the most?")

#Myteam.update({"Alistair": "Overeem"})
#print(Myteam)




# Skapa en tom dictionary
#person_info = {}

# Användarens input lagras i dictionaryn
#person_info["förnamn"] = input("Ange förnamn: ")  # Användaren skriver t.ex. "Khabib"
#person_info["efternamn"] = input("Ange efternamn: ")  # Användaren skriver t.ex. "Nurmagomedov"
#person_info["ålder"] = int(input("Ange ålder: "))  # Användaren skriver t.ex. 35
#person_info["stad"] = input("Ange stad: ")  # Användaren skriver t.ex. "Dagestan"

# Visa den ifyllda dictionaryn
#print(person_info)


#{
   # 'förnamn': 'Khabib',
   # 'efternamn': 'Nurmagomedov',
   # 'ålder': 35,
   # 'stad': 'Dagestan'
#}
