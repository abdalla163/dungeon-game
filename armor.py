import random

ARMOR_TYPES = {
    "Iron": {
        "Helm": 5,
        "Chestplate": 10,
        "Schoenen": 5
    },
    "Gold": {
        "Helm": 10,
        "Chestplate": 20,
        "Schoenen": 10
    },
    "Diamond": {
        "Helm": 15,
        "Chestplate": 30,
        "Schoenen": 15
    }
}

MATERIALS = ["Iron", "Gold", "Diamond"]


def maak_start_armor():
    return {
        "Helm": ("Iron", 5),
        "Chestplate": ("Iron", 10),
        "Schoenen": ("Iron", 5)
    }

def bereken_armor(armor):
    totaal = 0

    for onderdeel in armor.values():
        totaal += onderdeel["defense"]

    return totaal


def open_kist(armor, eindbaas_nummer):
    print("\n" + "=" * 40)
    print("🎁 ER VERSCHIJNT EEN SCHATKIST!")
    print("=" * 40)

    input("Druk op Enter om de kist te openen...")

    # Bepaal welk materiaal beschikbaar is.
    if eindbaas_nummer == 1:
        materiaal = "Iron"
    elif eindbaas_nummer == 2:
        materiaal = "Gold"
    else:
        materiaal = "Diamond"

    onderdeel = random.choice(list(ARMOR_TYPES[materiaal].keys()))
    waarde = ARMOR_TYPES[materiaal][onderdeel]

    print("\nJe opent de kist...")
    print(f"✨ Je hebt {materiaal} {onderdeel} gevonden!")
    print(f"🛡️ Dit onderdeel geeft {waarde} armor.")

    oude_armor = armor[onderdeel]

    if waarde > oude_armor[1]:
        armor[onderdeel] = (materiaal, waarde)
        print(f"Je {onderdeel} is verbeterd!")
    else:
        print("Je hebt dit onderdeel al op een hoger niveau.")
        print("Je huidige uitrusting blijft behouden.")

    print(f"\nJe totale armor is nu: {bereken_armor(armor)}")

    return armor


def toon_armor(armor):
    print("\n========== JOUW ARMOR ==========")

    for onderdeel, (materiaal, waarde) in armor.items():
        print(f"{materiaal} {onderdeel}: {waarde} armor")

    print("--------------------------------")
    print(f"Totale armor: {bereken_armor(armor)}")
    print("================================")
