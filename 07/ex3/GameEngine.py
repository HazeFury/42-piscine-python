from typing import Dict, Any, Optional, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """The main orchestrator of the card game."""

    def __init__(self) -> None:
        # Au départ, le moteur n'a ni usine, ni intelligence !
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    # L'INJECTION DE DÉPENDANCES EST ICI
    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        if not self.factory or not self.strategy:
            raise ValueError("Engine is missing factory or strategy!")

        # Le moteur sous-traite la création des cartes à l'Usine
        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell()
        ]
        self.cards_created += 3
        battlefield: List[Any] = []

        # Le moteur sous-traite la décision à la Stratégie
        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)

        return turn_result

    def get_engine_status(self) -> Dict[str, Any]:
        strat_name: str = (
            self.strategy.get_strategy_name() if self.strategy else "None"
        )
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strat_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
