from typing import Dict, Any, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform management system for card tournaments."""

    def __init__(self) -> None:
        self.registered_cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card to the platform."""
        self.registered_cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        """Simulate a match between two registered cards."""
        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]
        card1_health, card2_health = card1.health, card2.health,
        round = 0

        print(f"=======  Match #{self.matches_played}"
              f"  ({card1.name} vs {card2.name})  =======\n")
        while True:
            print(f"ROUND #{round}")
            if card1.is_alive():
                print(f"{card1.attack(card2.name)}")
                print(f"{card2.defend(card1.attack_power)}")
            else:
                winner, loser = card2, card1
                break
            print("--------------------------------------------")
            if card2.is_alive():
                print(f"{card2.attack(card1.name)}")
                print(f"{card1.defend(card2.attack_power)}")
            else:
                winner, loser = card1, card2
                break
            round += 1

        print(f"\nEND : {loser.name} has been defeated by {winner.name}."
              f" {winner.name} WON !")
        winner.update_wins(1)
        loser.update_losses(1)

        winner.rating += 16
        loser.rating -= 16

        self.matches_played += 1

        card1.health = card1_health
        card2.health = card2_health

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """Return all cards sorted by their rating (descending)."""
        sorted_cards = sorted(
            self.registered_cards.values(),
            key=lambda c: c.rating,
            reverse=True
        )
        return [c.get_tournament_stats() for c in sorted_cards]

    def generate_tournament_report(self) -> Dict[str, Any]:
        """Generate global platform statistics."""
        total_cards = len(self.registered_cards)
        avg_rating = 0

        if total_cards > 0:
            total_score = sum(c.rating for c in self.registered_cards.values())
            avg_rating = total_score // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
