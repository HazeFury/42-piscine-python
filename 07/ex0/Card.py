from abc import ABC, abstractmethod
from typing import Dict, Any


class Card(ABC):
    """Abstract base class representing a generic trading card."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Abstract method to play the card. Must be overridden."""
        pass

    def get_card_info(self) -> Dict[str, Any]:
        """Returns the basic information of the card."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Checks if the card can be played with the given mana."""
        return available_mana >= self.cost
