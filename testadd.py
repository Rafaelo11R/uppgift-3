fruitstore = {"Apple",
                 "Pear",
                  "Banana",
                  "Dates"
}

prices = {"Apple": 5,
            "Pear": 4,
            "Banana": 6,
            "Dates": 10
}


def add_fruit():       
    fruittype = input("What fruit do you want to add? (Apple, Pear, Banana, Dates) ").capitalize()
    measurements = int(input("How many pieces of this fruit? "))

    if fruittype in fruitstore:
        fruitstore[fruittype] += measurements
        print(f"Added {measurements} {fruittype} to the store")

    else:
        print("This fruit is not avaible")

    add_fruit()
    