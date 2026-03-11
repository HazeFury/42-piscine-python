from abc import ABC, abstractmethod
from typing import Dict, Any


class Combatable(ABC):
    """Abstract interface for cards capable of physical combat."""

    @abstractmethod
    def attack(self, target: str) -> Dict[str, Any]:
        """Perform an attack against a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Defend against incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        """Return the current combat statistics."""
        pass
