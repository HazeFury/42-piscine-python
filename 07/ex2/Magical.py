from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Magical(ABC):
    """Abstract interface for cards capable of using magic."""

    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: List[str]
            ) -> Dict[str, Any]:
        """Cast a specific spell on targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """Channel raw mana for magical use."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """Return the current magical statistics."""
        pass
