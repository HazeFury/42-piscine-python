from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck - Deck Builder ===")
    print("\nBuilding deck with different card types...\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    lightning = SpellCard("Lightning Bolt", 3, "Common",
                          "Deal 3 damage to target")
    crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3,
                           "Permanent: +1 mana per turn")

    my_deck = Deck()
    my_deck.add_card(dragon)
    my_deck.add_card(lightning)
    my_deck.add_card(crystal)

    print(f"Deck stats: {my_deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")
    my_deck.shuffle()

    for _ in range(3):
        drawn_card = my_deck.draw_card()
        if drawn_card:
            print(f"Drew: {drawn_card.name}"
                  f" ({getattr(drawn_card, 'type', 'Card')})")
            print(f"Play result: {drawn_card.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
