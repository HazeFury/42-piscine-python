from abc import ABC, abstractmethod
from typing import Dict, List, Union
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract Factory interface for creating game cards."""

    @abstractmethod
    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Create and return a new creature card."""
        pass

    @abstractmethod
    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Create and return a new spell card."""
        pass

    @abstractmethod
    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        """Create and return a new artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, List[Card]]:
        """Generate a complete themed deck of a specific size."""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, List[str]]:
        """Retrieve the catalog of card types supported by this factory."""
        pass
