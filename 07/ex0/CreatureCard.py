from typing import Dict, Any
from ex0.Card import Card


class CreatureCard(Card):
    """Concrete implementation of a creature card."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer.")

        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implements the abstract play method for a creature."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> Dict[str, Any]:
        """Specific method for creature combat."""
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict[str, Any]:
        """Overrides base method to include creature-specific stats."""
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })
        return info
