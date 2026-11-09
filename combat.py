
import random
from ui import speler_healthbar, vijand_healthbar
from inventory import item


def vechten(
    speler_health,
    healing_potions,
    super_healing_potions,
    strength_potions,
    strength_beurten,
    speler_naam,
    vijand_naam,
    vijand_health,
    vijand_attack,
    armor=0
):
    vijand_max_health = vijand_health

    while speler_health > 0 and vijand_health > 0:

        speler_healthbar(speler_naam, speler_health, armor)
        vijand_healthbar(vijand_naam, vijand_health, vijand_max_health)

        print("\nWat wil je doen?")
        print("1. Aanvallen")
        print("2. Inventory openen")
        print("3. Vluchten")

        keuze = input("> ").strip()

        if keuze == "1":
            schade = random.randint(10, 20)

            if strength_beurten > 0:
                schade *= 2
                strength_beurten -= 1

                print("\n💪 Strength Potion actief!")
                print(f"Je hebt nog {strength_beurten} versterkte aanvallen.")

            vijand_health -= schade

            print(f"\nJe doet {schade} schade aan {vijand_naam}!")

        elif keuze == "2":
            (
                speler_health,
                healing_potions,
                super_healing_potions,
                strength_potions,
                strength_beurten
            ) = item(
                speler_health,
                healing_potions,
                super_healing_potions,
                strength_potions,
                strength_beurten,
                speler_naam
            )

        elif keuze == "3":
            if random.random() < 0.3:
                print("\nJe bent succesvol gevlucht!")

                return (
                    speler_health,
                    healing_potions,
                    super_healing_potions,
                    strength_potions,
                    strength_beurten,
                    "gevlucht"
                )
            else:
                print("\nJe kon niet ontsnappen!")

        else:
            print("\nOngeldige keuze!")
            continue

        if vijand_health <= 0:
            break

        print(f"\n{vijand_naam} valt aan!")

        geblokkeerde_schade = min(armor, vijand_attack)
        ontvangen_schade = vijand_attack - geblokkeerde_schade

        speler_health -= ontvangen_schade

        print(f"🛡️ Je armor blokkeert {geblokkeerde_schade} schade!")
        print(f"❤️ Je ontvangt {ontvangen_schade} schade!")

    if speler_health <= 0:
        resultaat = "dood"

    elif "King" in vijand_naam:
        resultaat = "baas_gewonnen"

    else:
        resultaat = "gewonnen"

    return (
        speler_health,
        healing_potions,
        super_healing_potions,
        strength_potions,
        strength_beurten,
        resultaat
    )
