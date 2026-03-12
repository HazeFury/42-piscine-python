from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck - Tournament Platform ===")
    print("\nRegistering Tournament Cards...\n")

    dragon = TournamentCard(
        "Fire Dragon", 5, "Legendary", 7, 25, 3, "dragon_001", 1200
    )
    wizard = TournamentCard(
        "Ice Wizard", 4, "Epic", 4, 18, 2, "wizard_001", 1150
    )
    witcher = TournamentCard(
        "Neville Longdubras", 5, "Legendary", 3, 40, 2, "witcher_001", 1200
    )
    knight = TournamentCard(
        "Royal Knight", 4, "Rare", 6, 23, 4, "knight_001", 1200
    )

    platform = TournamentPlatform()
    platform.register_card(dragon)
    platform.register_card(wizard)
    platform.register_card(witcher)
    platform.register_card(knight)

    for card in [dragon, wizard]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("Interfaces: [Card, Combatable, Rankable]")
        print(f"Rating: {card.calculate_rating()}")
        print(f"Record: {card.wins}-{card.losses}\n")

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}\n")

    # print("Creating tournament match...")
    # match_result = platform.create_match("knight_001", "dragon_001")
    # print(f"Match result: {match_result}\n")

    # print("Creating tournament match...")
    # match_result = platform.create_match("witcher_001", "wizard_001")
    # print(f"Match result: {match_result}\n")

    # print("Creating tournament match...")
    # match_result = platform.create_match("knight_001", "witcher_001")
    # print(f"Match result: {match_result}\n")

    print("=======================\n"
          "Tournament Leaderboard:\n=======================")
    leaderboard = platform.get_leaderboard()
    for i, stats in enumerate(leaderboard, 1):
        print(f"{i}. {stats['name']} - Rating:"
              f" {stats['rating']} ({stats['record']})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
