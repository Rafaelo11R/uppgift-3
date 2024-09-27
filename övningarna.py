class Stations:
    def __init__(self, name, color, address):
        self.name = name
        self.color = color
        self.address = address

    @staticmethod
    def create_make():

        name_choice = input("Type the station")
        color_choice = input("Select the color")
        address_choice = input("Select the address")


        name = ["Huddinge", "Alby", "Nacka strand", "Bandhagen", "Solberga"]

        color = ["Pink", "Red", "Yellow", "Green", "Purple"]
    
        address = ["12354", "19290", "12471", "14281"]

        
        if name_choice == name:
            print(f"You choose {name}")

        elif color_choice == color:
            print(f"You chose color {color}")

        elif address_choice == address:
            print(f"You have {address_choice} as an address")

Stations.create_make()

    