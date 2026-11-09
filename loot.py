
import random

ARMOR_KIST = [
    ("Helm", 5),
    ("Chestplate", 10),
    ("Schoenen", 5)
]


def open_kist(armor, gevonden_armor):
    print("\n" + "=" * 40)
    print("🎁 EEN SCHATKIST VERSCHIJNT!")
    print("=" * 40)

    input("Druk op Enter om de kist te openen...")

    naam, waarde = random.choice(ARMOR_KIST)

    print("\nJe opent de kist...")
    print(f"✨ Je hebt gevonden: {naam}!")
    print(f"🛡️ +{waarde} armor!")

    armor += waarde
    gevonden_armor.append(naam)

    print(f"Je totale armor is nu: {armor}")

    return armor, gevonden_armor
