
def speler_healthbar(speler_naam, health, armor=0):
    print("\n" + "=" * 35)
    print(f"Speler: {speler_naam}")
    print(f"❤️ Health: {health}/100")
    print(f"🛡️ Armor: {armor}")
    print("=" * 35)


def vijand_healthbar(vijand_naam, health, max_health):
    print("\n" + "-" * 35)
    print(f"Vijand: {vijand_naam}")
    print(f"❤️ Health: {max(0, health)}/{max_health}")
    print("-" * 35)
