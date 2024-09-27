import os
class Station:
    def __init__(self, name, color, mailaddress):
        self.name = name
        self.color = color
        self.mailaddress = mailaddress

    def create_stations(self):
        name = ["Huddinge", "Alby", "Huvudsta", "Nacka strand", "Bro"]
        color = ["Pink", "Red", "Blue", "Yellow", "Pink"]
        mailaddress = ["12342", "19272", "14319", "18392", "14219"]

        name_choice = input("Type name of the station")
        color_choice = input("Type the color of the station")
        mailaddress_choice = input("Type mailaddress of the station")
        os.system('cls')

        if name_choice == name:
            print(f"You are visiting{name}")
        
        elif color_choice == color:
            print(color)

        elif mailaddress_choice == mailaddress:
            print(mailaddress)

        else:
            print("Invalid answer")

Station.create_stations()
    
