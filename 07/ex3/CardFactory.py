from abc import ABC, abstractmethod
from typing import Dict, List, Union
from ex0.Card import Card
from ex1.Deck import Deck


class CardFactory(ABC):
    """Abstract Factory interface for creating game cards."""

    @abstractmethod
    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        pass

    @abstractmethod
    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        pass

    @abstractmethod
    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Deck:
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, List[str]]:
        pass
