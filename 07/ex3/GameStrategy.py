from abc import ABC, abstractmethod
from typing import Dict, Any, List
from ex0.Card import Card


class GameStrategy(ABC):
    """Abstract interface for game AI strategies."""

    @abstractmethod
    def execute_turn(
        self, hand: List[Card], battlefield: List[Card]
            ) -> Dict[str, Any]:
        """Determine and execute the actions for a single turn."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        """Sort targets based on the strategy's priorities."""
        pass
