 # Program edytowany przez autora Bartłomieja Ostrowskiego v.1.1
# Program obliczający pole prostokąta


# Program obliczający pole prostokąta z użyciem pętli while

while True:
    dlugosc = float(input("Podaj długość boku a: "))
    szerokosc = float(input("Podaj długość boku b: "))

    pole = dlugosc * szerokosc

    print("Pole prostokąta wynosi: ", pole)

    odp = input("Czy chcesz kontynuować (t/n)? ")
    if odp.lower() == "n":
        break