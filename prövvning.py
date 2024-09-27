import os

class Station:
    stations = ["Huddinge", "Alby", "Nacka strand", "Solna stand", "Huvudsta"]
    color = ["Pink", "Red", "Yellow", "Blue", "Blue"]
    mailadress = ["12371", "14591", "19243", "16592", "16391"]
    

# Skapa en instans av klassen
#station1 = Station("Blue", "example@mail.com")
    
    os.system('cls' if os.name == "nt" else "clear")

    @staticmethod
    def visit_station():
        user_choice = input("Which station do you want to visit? ")
        
        if user_choice in Station.stations:
            print(f"You are visiting {user_choice}.")
        else:
            print("This station does not exist.")

    os.system('cls' if os.name == "nt" else "clear")

    @staticmethod
    def chosing_color():
        user_choice = input("Type the color")

        if user_choice in Station.color:
            print(f"The color is {user_choice}")

        else:
            print("Invalid color")

    os.system('cls' if os.name == "nt" else "clear")

    @staticmethod
    def type_mailaddress():
        user_choice = input("Type the mailaddress")

        if user_choice in Station.mailadress:
            print(f"The mailaddress is {user_choice}")

        else: 
            print("Please type the mailaddress")






# Skapa en instans av klassen
#station1 = Station("Blue", "example@mail.com")
Station.visit_station()  # Här anropar vi metoden för att få input
Station.chosing_color()
Station.type_mailaddress()


#stations = ["Huddinge", "Alby", "Nacka strand", "Solna stand", "Huvudsta"]
   # color = ["Pink", "Red", "Yellow", "Blue", "Blue"]
    #mailadress = ["12371", "14591", "19243", "16592", "16391"]


