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


# Roep de vechten() functie aan met de naam, health en damage van de vijand.
# Bijvoorbeeld: vechten("Goblin", 80, 25)
def vechten(vijand_naam, vijand_health, vijand_damage):
    speler_health = 100

    while speler_health > 0 and vijand_health > 0:
        speler_attack = 20
        vijand_health = vijand_health - speler_attack
        print("Je valt de", vijand_naam, "aan!")
        print("De", vijand_naam, "verliest", speler_attack, "HP")
        print("Enemy health:", vijand_health)
        if vijand_health <= 0:
            print("Je hebt de", vijand_naam, "verslagen!")
        else:
            speler_health = speler_health - vijand_damage
            print("De", vijand_naam, "valt jou aan!")
            print("Je verliest", vijand_damage, "HP")
            print("Jouw health:", speler_health)
    if speler_health <= 0:
        print("Je bent dood GAME OVER")


def deuren():
    print("Je hebt de goblin verslagen!")
    print("Je loopt verder de dungeon in.")
    print("Je komt in een grote kamer.")
    print("Voor je staan twee deuren.")
    print("1. De linker deur")
    print("2. De rechter deur")

    keuze = input("Welke deur kies je? ")

    if keuze == "1":
        print("Je komt in een oude opslagkamer")
        print("Je vindt een zwaard!")
        return 1
    elif keuze == "2":
        print("Je komt in een donkere kamer.")
        return 2

    else:
        print("Ongeldige keuze!")
        return 0


def main():
    print("naam van onze game: quest for the cure")
    begin()

    keuze = input("wat wil je doen? ")
    if keuze == "1":
        vechten("goblin", 50, 15)

        keuze_deur = deuren()
        if keuze_deur == 1:
            print("Je neemt het zwaard mee")
            print("Je loopt naar de volgende kamer")
            print("Je ziet een grotere goblin hij noemt zichzelf de goblin koning")

            print("1. Val de goblin koning aan.")
            print("2. Ren weg")
            keuze = input("wat wil je doen? ")
            if keuze == "1":
                vechten("goblin koning", 80, 30)
            elif keuze == "2":
                print("Je rent naar een andere kamer")
            else:
                print("Ongeldige keuze")

        elif keuze_deur == 2:
            print("Je hoort iets.....")
            vechten("skeleton", 65, 20)
    elif keuze == "2":
        weglopen()
    else:
        print("Ongeldige keuze")


if __name__ == "__main__":
    main()
