from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A comprehensive card ready for tournament platform play."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int,
        defense: int, card_id: str, base_rating: int = 1200
    ) -> None:
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health
        self.defense_power = defense

        self.card_id = card_id
        self.rating = base_rating
        self.wins = 0
        self.losses = 0
        self.type = "Tournament"

    def is_alive(self) -> bool:
        return self.health > 0

    # #######################  Card  #######################
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {"card_played": self.name, "effect": "Enters the arena"}

    # ####################  Combatable  ####################
    def attack(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
            }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = min(incoming_damage, self.defense_power)
        damage_taken = incoming_damage - blocked
        self.health = max(self.health - damage_taken, 0)
        return {
            "defender": self.name,
            "damage taken": damage_taken,
            "health left": self.health,
            "still_alive": self.health > 0
            }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "attack": self.attack_power,
            "defense": self.defense_power,
            "health": self.health
            }

    # #####################  Rankable  ####################
    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> Dict[str, Any]:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
            }

    # #####################  Specific  ####################
    def get_tournament_stats(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
