import random
from combat import vechten
from data import get_enemies, get_bosses


def random_vijand(
    health,
    healing_potions,
    super_healing_potions,
    strength_potions,
    strength_beurten,
    speler_naam,
    armor=0,
    boss=None
):
    # Haal de enemies en bosses op uit data.py
    ENEMIES = get_enemies()
    BOSSES = get_bosses()

    # Controleer of er een boss gekozen moet worden
    if boss is not None:
        vijand = None

        for baas in BOSSES:
            if baas["name"] == boss:
                vijand = baas
                break

        if vijand is None:
            print(f"Boss '{boss}' bestaat niet!")
            return (
                "gewonnen",
                health,
                healing_potions,
                super_healing_potions,
                strength_potions,
                strength_beurten,
                None
            )

    else:
        # Kies een willekeurige normale vijand
        vijand = random.choice(ENEMIES)

    print(f"\nEr verschijnt een {vijand['name']}!")
    print(f"Health: {vijand['health']}")
    print(f"Aanval: {vijand['attack']}")

    # Start het gevecht
    (
        health,
        healing_potions,
        super_healing_potions,
        strength_potions,
        strength_beurten,
        resultaat
    ) = vechten(
        health,
        healing_potions,
        super_healing_potions,
        strength_potions,
        strength_beurten,
        speler_naam,
        vijand["name"],
        vijand["health"],
        vijand["attack"],
        armor
    )

    # Geef alle gegevens terug aan main.py
    return (
        resultaat,
        health,
        healing_potions,
        super_healing_potions,
        strength_potions,
        strength_beurten,
        vijand["name"]
    )
