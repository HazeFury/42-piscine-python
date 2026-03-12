from abc import ABC, abstractmethod
from typing import Dict, Any


class Rankable(ABC):
    """Abstract interface for tournament ranking capabilities."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current ranking rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Add to the total number of wins."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Add to the total number of losses."""
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict[str, Any]:
        """Return the complete ranking statistics."""
        pass
