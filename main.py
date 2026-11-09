import time

from enemies import random_vijand
from ui import speler_healthbar
from armor import bereken_armor, open_kist, toon_armor
from dungeon import get_kamers



def main():
    print("================================")
    print("       QUEST FOR THE CURE")
    print("================================")

    speler_naam = input("\nWat is je naam, avonturier? ")

    # Speler begint zonder armor
    health = 100
    armor = {}

    # Potions
    healing_potions = 3
    super_healing_potions = 1
    strength_potions = 2
    strength_beurten = 0

    print(f"\nWelkom {speler_naam}!")
    print("Je begint aan je avontuur om de cure te vinden.")

    speler_healthbar(health, speler_naam)


   

    # Loop door alle kamers van de dungeon
    kamers = get_kamers()
    for kamer in kamers:
        print(kamer["naam"])

        # Eindkamer met de cure
        if kamers["type"] == "geneesmiddel":

            print("\nJe hebt de laatste kamer bereikt!")

            time.sleep(2)
            print("\nEr verschijnt een mysterieuze kist...")

            time.sleep(2)
            print("Je opent de kist...")

            time.sleep(2)
            print("In de kist ligt de cure!")

            time.sleep(2)
            print(f"\n{speler_naam}, je hebt de cure gevonden!")

            time.sleep(2)
            print(f"{speler_naam}, je kunt je vrouw redden! ❤️")

            time.sleep(2)
            print("\nJe verlaat de dungeon.")

            time.sleep(2)
            print("Je gaat terug naar je vrouw.")

            time.sleep(2)
            print("Je geeft haar de cure.")

            time.sleep(2)
            print("Ze is genezen!")

            time.sleep(2)
            print("\n========== EINDE ==========")

            break

        # Bepaal of de kamer een eindbaas bevat
        if kamers["type"] == "eindbaas":
            baas_naam = kamers["vijand"]
            print(f"\nPas op! Je staat tegenover {baas_naam}!")

            totaal_armor = bereken_armor(armor)

            (
                resultaat,
                health,
                healing_potions,
                super_healing_potions,
                strength_potions,
                strength_beurten,
                vijand_naam
            ) = random_vijand(
                health,
                healing_potions,
                super_healing_potions,
                strength_potions,
                strength_beurten,
                speler_naam,
                totaal_armor,
                boss=baas_naam
            )

        else:
            # Normale vijand
            totaal_armor = bereken_armor(armor)

            (
                resultaat,
                health,
                healing_potions,
                super_healing_potions,
                strength_potions,
                strength_beurten,
                vijand_naam
            ) = random_vijand(
                health,
                healing_potions,
                super_healing_potions,
                strength_potions,
                strength_beurten,
                speler_naam,
                totaal_armor
            )

        # Controleer of de speler dood is
        if resultaat == "dood":
            print("\n================================")
            print("             GAME OVER")
            print("================================")
            print(f"{speler_naam} heeft de dungeon niet overleefd.")
            return

        # Controleer of de speler gevlucht is
        if resultaat == "gevlucht":
            print("\nJe bent gevlucht uit het gevecht!")
            print("Je avontuur is voorbij.")
            return

        # Geef armor wanneer een eindbaas verslagen is
        if resultaat == "baas_gewonnen":

            print("\n================================")
            print("       EINDbaas VERSLAGEN!")
            print("================================")

            time.sleep(2)
            print("Er verschijnt een mysterieuze kist...")

            time.sleep(2)
            print("Je opent de kist...")

            # Geef een armor-onderdeel
            armor = open_kist(armor, kamers["nummer"] // 3)

            time.sleep(1)
            print("\nDit is je huidige armor:")
            toon_armor(armor)

        # Toon de overgebleven potions
        print("\n================================")
        print("          INVENTORY")
        print("================================")
        print(f"Healing Potions: {healing_potions}")
        print(f"Super Healing Potions: {super_healing_potions}")
        print(f"Strength Potions: {strength_potions}")

        print(f"\nHealth: {health}/100")

        totaal_armor = bereken_armor(armor)
        print(f"Totale armor: {totaal_armor}")

    print("\n================================")
    print("       EINDE VAN HET AVONTUUR")
    print("================================")

    print(f"Speler: {speler_naam}")
    print(f"Overgebleven health: {health}")

    print("\nJe uiteindelijke armor:")
    toon_armor(armor)


if __name__ == "__main__":
    main()
