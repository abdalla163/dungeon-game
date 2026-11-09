from ui import speler_healthbar


def item(speler_health, healing_potions, super_healing_potions,
         strength_potions, strength_beurten, speler_naam):

    while True:
        print("\n========== INVENTORY ==========")
        print(f"1. Healing Potion ({healing_potions})")
        print(f"2. Super Healing Potion ({super_healing_potions})")
        print(f"3. Strength Potion ({strength_potions})")
        print("4. Terug")
        print("===============================")

        keuze = input("Welk item wil je gebruiken? ").strip()

        if keuze == "1":
            if healing_potions > 0:
                oude_health = speler_health
                speler_health = min(100, speler_health + 30)
                healing_potions -= 1
                print("\nJe gebruikt een Healing Potion!")
                speler_healthbar(speler_naam, speler_health)
                print(f"Je HP is hersteld van {oude_health} naar {speler_health}!")
                return (speler_health, healing_potions, super_healing_potions,
                        strength_potions, strength_beurten)
            print("Je hebt geen Healing Potions meer!")

        elif keuze == "2":
            if super_healing_potions > 0:
                oude_health = speler_health
                speler_health = min(100, speler_health + 60)
                super_healing_potions -= 1
                print("\nJe gebruikt een Super Healing Potion!")
                speler_healthbar(speler_naam, speler_health)
                print(f"Je HP is hersteld van {oude_health} naar {speler_health}!")
                return (speler_health, healing_potions, super_healing_potions,
                        strength_potions, strength_beurten)
            print("Je hebt geen Super Healing Potions meer!")

        elif keuze == "3":
            if strength_potions > 0:
                strength_potions -= 1
                strength_beurten = 3
                print("\nJe gebruikt een Strength Potion!")
                print("Je aanvalsschade is nu verdubbeld!")
                print("De werking duurt 3 aanvallen.")
                return (speler_health, healing_potions, super_healing_potions,
                        strength_potions, strength_beurten)
            print("Je hebt geen Strength Potions meer!")

        elif keuze == "4":
            print("Je gaat terug naar het gevecht.")
            return (speler_health, healing_potions, super_healing_potions,
                    strength_potions, strength_beurten)
        else:
            print("Ongeldige keuze!")
