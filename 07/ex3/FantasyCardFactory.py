from typing import Dict, List, Union
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """Concrete factory generating fantasy-themed cards."""

    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if str(name_or_power).lower() == "dragon" or name_or_power == 5:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 5, 2)

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        return SpellCard(
            "Lightning Bolt", 3, "Common", "Deal 3 damage to target"
        )

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        return ArtifactCard(
            "Mana Ring", 2, "Rare", 3, "Permanent: +1 mana per turn"
        )

    def create_themed_deck(self, size: int) -> Dict[str, List[Card]]:
        themed_deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }

        cards_per_type = size // 3
        remaining_cards = size % 3

        for _ in range(cards_per_type):
            themed_deck["creatures"].append(self.create_creature("goblin"))
            themed_deck["spells"].append(self.create_spell())
            themed_deck["artifacts"].append(self.create_artifact())

        for _ in range(remaining_cards):
            themed_deck["creatures"].append(self.create_creature("goblin"))

        return themed_deck

    def get_supported_types(self) -> Dict[str, List[str]]:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
