from typing import Dict, Any, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """A powerful card combining base mechanics, combat, and magic."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, defense: int,
        health: int, mana_capacity: int, combat_type: str
    ) -> None:
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.defense_power = defense
        self.health = health
        self.mana_capacity = mana_capacity
        self.combat_type = combat_type
        self.type = "Elite"

    # #######################  Card  #######################
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite champion enters the battlefield!"
        }

    # ####################  Combatable  ####################
    def attack(self, target: str) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = min(incoming_damage, self.defense_power)
        damage_taken = incoming_damage - blocked
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack": self.attack_power,
            "defense": self.defense_power,
            "health": self.health
        }

    # #####################  Magical  ####################
    def cast_spell(
            self, spell_name: str, targets: List[str]
            ) -> Dict[str, Any]:
        mana_cost = 4
        self.mana_capacity -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana_capacity += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_capacity
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {"mana_capacity": self.mana_capacity}
