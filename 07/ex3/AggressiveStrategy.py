from typing import Dict, Any, List
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    """Concrete strategy favoring fast attacks and low-cost cards."""

    def execute_turn(
        self, hand: List[Card], battlefield: List[Card]
    ) -> Dict[str, Any]:

        cards_played = []
        mana_used = 0
        damage = 0
        max_mana = 5

        hand.sort(key=lambda c: c.cost)

        for card in hand:
            if mana_used + card.cost <= max_mana:
                cards_played.append(card.name)
                mana_used += card.cost

                if getattr(card, "type", "") == "Creature":
                    damage += getattr(card, "attack", 0)
                elif getattr(card, "type", "") == "Spell":
                    damage += 3

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        """Always prioritize the Enemy Player."""
        if "Enemy Player" in available_targets:
            return ["Enemy Player"] + [
                t for t in available_targets if t != "Enemy Player"
                ]
        return available_targets
