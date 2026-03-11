from typing import Dict, Any
from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete implementation of an artifact card."""

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Artifacts remain in play until destroyed[cite: 662]."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> Dict[str, Any]:
        """Implements activate_ability for ongoing effects[cite: 661]."""
        self.durability -= 1
        return {
            "artifact_activated": self.name,
            "remaining_durability": self.durability,
            "effect": self.effect
        }

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info.update({"type": self.type, "durability": self.durability})
        return info
