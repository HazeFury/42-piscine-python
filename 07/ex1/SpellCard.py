from typing import Dict, Any, List
from ex0.Card import Card


class SpellCard(Card):
    """Concrete implementation of a spell card."""

    def __init__(
            self, name: str, cost: int, rarity: str, effect_type: str
            ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Spells are consumed when played (one-time use)."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: List[str]) -> Dict[str, Any]:
        """Implements resolve_effect for spell mechanics."""
        return {
            "spell_resolved": self.name,
            "targets_affected": targets,
            "effect_type": self.effect_type
        }

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info.update({"type": self.type, "effect_type": self.effect_type})
        return info
