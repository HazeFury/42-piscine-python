import random
from math import ceil
from typing import List, Dict, Any, Optional
from ex0.Card import Card


class Deck:
    """Deck management system for trading cards."""

    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a new card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by its name."""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomly shuffle the cards in the deck."""
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """Draw the top card from the deck."""
        if self.cards:
            return self.cards.pop()
        return None

    def get_deck_stats(self) -> Dict[str, Any]:
        """Calculate and return stats about the current state of the deck."""
        if not self.cards:
            return {"total_cards": 0, "avg_cost": 0.0}

        stats: Dict[str, Any] = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
        }

        total_cost = 0
        for card in self.cards:
            total_cost += card.cost
            card_type = getattr(card, "type", "Unknown").lower()
            if card_type + "s" in stats:
                stats[card_type + "s"] += 1

        stats["avg_cost"] = float(ceil(total_cost / len(self.cards)))
        return stats
