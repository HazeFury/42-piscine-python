from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck - Ability System ===\n")
    print("EliteCard capabilities:")

    card_methods = [m for m in dir(Card) if not m.startswith('_')]
    combat_methods = [m for m in dir(Combatable) if not m.startswith('_')]
    magic_methods = [m for m in dir(Magical) if not m.startswith('_')]
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    arcane_warrior = EliteCard(
        name="Arcane Warrior", cost=6, rarity="Mythic",
        attack=5, defense=3, health=8, mana_capacity=8, combat_type="melee"
    )

    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}\n")

    print("Magic phase:")
    print("Spell cast: "
          f"{arcane_warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}\n")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
