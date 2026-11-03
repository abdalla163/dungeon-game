import time

def begin():
    print("Mijn vrouw is ziek alleen in de dungeon kan ik de cure vinden.")
    print("1. De dungeon binnengaan")
    print("2. Weglopen")


def weglopen():
    print("Je besluit weg te lopen.")
    print("Je laat de zoektocht naar de cure achter je.")


# Roep de vechten() functie aan met de naam, health en damage van de vijand.
# Bijvoorbeeld: vechten("Goblin", 80, 25)
def vechten(
    vijand_naam, vijand_health, vijand_attack, speler_health=100, speler_attack=20
):
    

    print(f"Een {vijand_naam} valt je aan \n")

    while speler_health > 0 and vijand_health > 0:
        menu = input("1. Aanvallen 2. Wegrennen\n ")
        if menu == "1":
            vijand_health = max(0, vijand_health - speler_attack)
            time.sleep(1.5)
            print(f"Je valt de {vijand_naam} (-{speler_attack}) | {vijand_naam.capitalize()}: {vijand_health} HP \n")
            
        elif menu == "2":
            weglopen()
            return speler_health, "gevlucht"
        else:
            print("Ongeldige Keuze")
            continue
        if vijand_health > 0:
            speler_health = max(0, speler_health - vijand_attack)
            print(f"De {vijand_naam} valt je aan en doet (-{vijand_attack}) schade | Jij: {speler_health} HP \n")
        else:
            break
    if speler_health <= 0:
        print("Je bent dood GAME OVER")
        return speler_health, "dood"
    
    
    print(f"Je hebt de {vijand_naam} verslagen! \n")
    return speler_health, "gewonnen"


# time.sleep()


def deuren():
    print("Je loopt verder de dungeon in en je ziet twee deuren voor je.\n")
    print("Welke deur kies jij? \n")
    print("1. De linker deur")
    print("2. De rechter deur")

    keuze = input("Welke deur kies je? ")

    if keuze == "1":
        print("Je komt in een oude opslagkamer")
        print("Je vindt een zwaard! \n")
        return 1
    elif keuze == "2":
        print("Je komt in een donkere kamer. \n")
        return 2

    else:
        print("Ongeldige keuze!")
        return 0


def main():
    print("Quest for the cure \n")
    begin()

    keuze = input("wat wil je doen? ")
    if keuze == "1":
        vechten("goblin", 50, 15)

        keuze_deur = deuren()
        if keuze_deur == 1:
            print("Je neemt het zwaard mee en je loopt naar de volgende kamer.")
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
            print("Je hoort iets..... \n")
            vechten("skeleton", 65, 20)
    elif keuze == "2":
        weglopen()
    else:
        print("Ongeldige keuze")


if __name__ == "__main__":
    main()
