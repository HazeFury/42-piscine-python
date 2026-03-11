from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck - Game Engine ===")
    print("Configuring Fantasy Card Game...\n")

    # 1. On crée nos dépendances
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    # 2. On crée le moteur et on lui INJECTE les dépendances
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")

    print("Turn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")

    # Le moteur fait tout le travail tout seul !
    actions = engine.simulate_turn()
    print(f"Actions: {actions}\n")

    print("Game Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
