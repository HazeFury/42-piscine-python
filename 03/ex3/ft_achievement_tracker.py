def main() -> None:
    """Analyzes player achievements using set operations."""
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {"first_kill", "level_10", "treasure_hunter",
                       "speed_demon"}

    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}

    charlie: set[str] = {"level_10", "treasure_hunter", "boss_slayer",
                         "speed_demon", "perfectionist"}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements: set[str] = alice.union(bob, charlie)

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all: set[str] = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}")

    alice_only = alice.difference(bob, charlie)
    bob_only = bob.difference(alice, charlie)
    charlie_only = charlie.difference(alice, bob)

    rare_achievements: set[str] = alice_only.union(bob_only, charlie_only)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    alice_bob_common: set[str] = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique: set[str] = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique: set[str] = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
