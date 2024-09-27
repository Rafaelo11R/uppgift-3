import os

while True:
    os.system('cls')

    print("Vällkommen in till miniräknaren")
    user_choice = input("Vad vill du beräkna? (*, //, /, -, +,)")

    def berakna_subtration(num1, num2):
        resultat = num1 - num2

        print(f"{num1} - {num2} = {resultat} Bra jobbat!")

    def berakna_divitionfloat(num1, num2):
        resultat = num1 / num2
        print(f"{num1} / {num2} = {resultat} Bra jobbat!")


    def berakna_addition(num1, num2):
        resultat = num1 + num2

        print(f"{num1} + {num2} = {resultat} Bra jobbat!")



    def berakna_divition(num1, num2):
        resultat = num1 // num2

        print(f"{num1} // {num2} = {resultat} Bra jobbat!")


    def berakna_multiplikation(num1, num2):
        resultat = num1 * num2

        print(f"{num1} * {num2} = {resultat}")

    num1 = int(input("Ange ett tal"))
    num2 = int(input("Ange ett tal"))

    os.system('cls')

    if user_choice == "*":
        berakna_multiplikation(num1, num2)
    

    elif user_choice == "//":
        berakna_divition(num1, num2)

    elif user_choice == "-":
        berakna_subtration(num1, num2)

    elif user_choice == "+":
        berakna_addition(num1, num2)

    elif user_choice == "/":
        berakna_divitionfloat(num1, num2)

    else:
        print("Ogiligt svar")

    forsatta = input("Vill du fortsätta? (Ja/Nej)")

    if forsatta == "Nej":
        print("Tack för du använde miniräknaren")
        break
    
    elif forsatta =="Ja":
        print("Vällkommen igen")

    else:
        print("Ogiltigt Svar")

     
        







