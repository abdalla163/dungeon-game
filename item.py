import time
import random


def begin():
    print("Mijn vrouw is ziek. Alleen in de dungeon kan ik de cure vinden.")
    print("1. De dungeon binnengaan")
    print("2. Vluchten")


def weglopen():
    print("Je besluit weg te lopen.")
    print("Je laat de zoektocht naar de cure achter je.")


def vluchten(vijand_naam, speler_health):
    kans = random.randint(1, 100)

    if kans <= 30:
        print("Het is gelukt! Je bent ontsnapt!\n")
        print("Je komt terecht in een andere kamer.\n")

        deuren()

        return speler_health, "gevlucht"

    else:
        print("Het ontsnappen is mislukt!\n")
        print(f"{vijand_naam} valt je weer aan.")

        return speler_health, "mislukt"


# Healing Potion gebruiken
def item(speler_health, healing_potions):

    if healing_potions > 0:
        oude_health = speler_health

        speler_health = min(100, speler_health + 30)
        healing_potions -= 1

        print("Je gebruikt een Healing Potion!")
        print(f"Je HP is hersteld van {oude_health} naar {speler_health}!")

    else:
        print("Je hebt geen Healing Potions meer!")

    return speler_health, healing_potions


# Healthbar van de speler
def speler_healthbar(health):
    totaal = 100
    blokjes = int(health / totaal * 20)

    if health >= 60:
        kleur = "\033[92m"
        status = "Gezond"

    elif health >= 30:
        kleur = "\033[93m"
        status = "Gewond"

    else:
        kleur = "\033[91m"
        status = "KRITIEK!"

    reset = "\033[0m"

    balk = kleur + "█" * blokjes + reset + "░" * (20 - blokjes)

    print(f"HP: [{balk}] {health}/{totaal} - {status}")

    if health <= 29:
        print("WAARSCHUWING! Je hebt bijna geen levens meer!")


# Healthbar van de vijand
def vijand_healthbar(health):
    totaal = 120
    blokjes = int(health / totaal * 50)

    if health >= 60:
        kleur = "\033[92m"

    elif health >= 30:
        kleur = "\033[93m"

    else:
        kleur = "\033[91m"

    reset = "\033[0m"

    balk = kleur + "█" * blokjes + reset + "░" * (50 - blokjes)

    print(f"HP: [{balk}] {health}/{totaal}")


# Gevecht met een vijand
def vechten(vijand_naam, vijand_health, vijand_attack,
            speler_health=100, speler_attack=20, healing_potions=2):

    print(f"Een {vijand_naam} valt je aan!\n")

    speler_healthbar(speler_health)
    vijand_healthbar(vijand_health)

    while speler_health > 0 and vijand_health > 0:

        menu = input("1. Aanvallen 2. Items 3. Wegrennen\n ")

        if menu == "1":
            vijand_health = max(0, vijand_health - speler_attack)

            time.sleep(1.5)

            print(f"Je valt de {vijand_naam} aan (-{speler_attack})")
            print(f"{vijand_naam} verliest {speler_attack} HP\n")

        elif menu == "2":
            speler_health, healing_potions = item(
                speler_health, healing_potions
            )

        elif menu == "3":
            speler_health, status = vluchten(
                vijand_naam, speler_health
            )

            if status == "gevlucht":
                return speler_health, "gevlucht", healing_potions

        else:
            print("Ongeldige keuze!")
            continue

        # Toon de actuele HP van speler en vijand
        speler_healthbar(speler_health)
        vijand_healthbar(vijand_health)

        # De vijand valt terug aan als hij nog leeft
        if vijand_health > 0:
            speler_health = max(0, speler_health - vijand_attack)

            print(f"\nDe {vijand_naam} valt je aan!")
            print(f"Je verliest {vijand_attack} HP\n")

            speler_healthbar(speler_health)

    if speler_health <= 0:
        print("Je bent dood GAME OVER!")
        return speler_health, "dood", healing_potions

    print(f"Je hebt de {vijand_naam} verslagen!\n")

    return speler_health, "gewonnen", healing_potions


# De deuren van de dungeon
def deuren():
    print("Je loopt verder de dungeon in en je ziet twee deuren voor je.\n")
    print("Welke deur kies jij?")
    print("1. De linker deur")
    print("2. De rechter deur")

    keuze = input("Welke deur kies je? ")

    if keuze == "1":
        print("Je komt in een oude opslagkamer.")
        print("Je vindt een zwaard!")
        return 1

    elif keuze == "2":
        print("Je komt in een donkere kamer.")
        return 2

    else:
        print("Ongeldige keuze")
        return 0


# Hoofdprogramma
def main():
    print("Quest for the cure\n")

    # De speler begint met 2 Healing Potions
    healing_potions = 2

    begin()

    keuze = input("Wat wil je doen? ")

    if keuze == "1":

        keuze_deur = deuren()

        if keuze_deur == 1:
            print("Je neemt het zwaard mee en loopt naar de volgende kamer.")
            print("Je ziet een grotere goblin: de goblin koning!")

            speler_health, resultaat, healing_potions = vechten(
                "goblin koning",
                120,
                30,
                speler_attack=50,
                healing_potions=healing_potions
            )

            if resultaat == "gewonnen":
                print("\nJe hebt de Goblin Koning verslagen!")
                print("Er verschijnt een mysterieuze kist...")
                time.sleep(2)

                print("Je opent de kist...")
                time.sleep(2)

                print("In de kist ligt de cure!")
                time.sleep(2)

                print("Je hebt de cure gevonden!")
                time.sleep(2)

                print("Je kunt je vrouw redden! ❤️")
                time.sleep(2)

                print("Je verlaat de dungeon.")
                time.sleep(2)

                print("Je gaat terug naar je vrouw.")
                time.sleep(2)

                print("Je geeft haar de cure.")
                time.sleep(2)

                print("Ze is genezen!")
                time.sleep(2)

                print("Einde!")

        elif keuze_deur == 2:
            print("Je hoort iets.....")

            speler_health, resultaat, healing_potions = vechten(
                "skeleton",
                65,
                20,
                healing_potions=healing_potions
            )

    elif keuze == "2":
        weglopen()

    else:
        print("Ongeldige keuze!")


if __name__ == "__main__":
    main()
