from typing import Dict, List, Union
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


class FantasyCardFactory(CardFactory):
    """Concrete factory generating fantasy-themed cards."""

    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        # Si on demande un dragon ou une puissance de 5, on renvoie le boss
        if str(name_or_power).lower() == "dragon" or name_or_power == 5:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        # Sinon, par défaut, on renvoie une carte pas chère pour l'IA agressive
        # On lui donne 5 d'attaque pour coller au calcul de dégâts du PDF !
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

    def create_themed_deck(self, size: int) -> Deck:
        deck = Deck()
        for _ in range(size // 3):
            deck.add_card(self.create_creature("goblin"))
            deck.add_card(self.create_spell())
            deck.add_card(self.create_artifact())
        return deck

    def get_supported_types(self) -> Dict[str, List[str]]:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
