def begin():
    print("main character: de man die ze vrouw red")
    print("zijn vrouw is ziek")
    print("hij gaat naar de dungeon om ze vrouw te redden")
    print("1. De dungeon binnengaan")
    print("2. Weglopen")

def weglopen():
    print("weglopen")
    print("Je besluit weg te lopen.")
    print("Je laat de zoektocht naar de cure achter je.")


def main():
    print("naam van onze game: quest for the cure")
    begin()

    keuze = input("wat wil je doen?")

    if keuze == "1":
        print("De dungeon binnengaan")
        print("Het is donker en stil.")
        print("Plotseling verschijnt er een goblin!")
        print("1. Aanvallen!")
        print("2. Wegrennen")
        keuze = input("Wat wil je doen? ")
        if keuze == "1":
            print ("je hebt de goblin verslagen!")
            print("Je loopt verder de dungeon in.")
            print("Je komt in een grote kamer.")
            print("Voor je staan twee deuren.")
            print("1. De linker deur")
            print("2. De rechter deur")
            keuze = input("Welke deur kies je? ")
            if keuze == "1":
                print("Je komt in een oude opslagkamer")
                print("je vindt een zwaard!")
            else:
                print("Je komt in een donkere kamer")
                print("er is een skeleton voor je!")
                print("Skeleton valt je aan!")
                print("1. Aanvallen!")
                print("2. Wegrennen!")
                keuze = input("wat wil je doen?")
                if keuze == "1":
                    print("je hebt de skeleton verslagen!")

                

        else:
            print("wegrennen!")
            print("Je rent weg van de goblin.")
            print("Je rent terug naar de ingang van de dungeon.")
            print("Je hebt de dungeon niet kunnen bereiken.")
    else:
        weglopen()


if __name__ == "__main__":
    main()