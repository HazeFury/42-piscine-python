def main() -> None:
    """Runs the analytics dashboard using comprehensions."""

    data: list[tuple[str, int, str, tuple[str, ...]]] = [
        ("alice", 2300, "north", ("first_kill", "level_10", "boss_slayer")),
        ("bob", 1800, "east", ("first_kill",)),
        ("charlie", 2150, "central", ("boss_slayer", "level_10")),
        ("diana", 2050, "north", ("first_kill", "pacifist", "collector"))
    ]

    print("=== Game Analytics Dashboard ===\n")

    # ################  List Comprehension Examples  ################
    print("=== List Comprehension Examples ===")

    high: list[str] = [n for n, s, _, _ in data if s > 2000]
    print(f"High scorers (>2000): {high}")

    doubled: list[int] = [s * 2 for _, s, _, _ in data]
    print(f"Scores doubled: {doubled}")

    active: list[str] = [n for n, _, _, _ in data]
    print(f"Active players: {active}\n")

    # ################  Dict Comprehension Examples  ################
    print("=== Dict Comprehension Examples ===")

    p_scores: dict[str, int] = {n: s for n, s, _, _ in data}
    print(f"Player scores: {p_scores}")

    cats: dict[str, str] = {
        n: "high" if s > 2000 else "medium" for n, s, _, _ in data
    }
    print(f"Score categories: {cats}")

    a_counts: dict[str, int] = {n: len(ach) for n, _, _, ach in data}
    print(f"Achievement counts: {a_counts}\n")

    # ################  Set Comprehension Examples  ################
    print("=== Set Comprehension Examples ===")

    u_players: set[str] = {n for n, _, _, _ in data}
    print(f"Unique players: {u_players}")

    u_achiev: set[str] = {
        ach for _, _, _, ach_tup in data for ach in ach_tup
    }
    print(f"Unique achievements: {u_achiev}")

    regions: set[str] = {r for _, _, r, _ in data}
    print(f"Active regions: {regions}\n")

    # ####################  Combined Analysis  ####################
    print("=== Combined Analysis ===")
    print(f"Total players: {len(u_players)}")
    print(f"Total unique achievements: {len(u_achiev)}")

    avg: float = sum([s for _, s, _, _ in data]) / len(data)
    print(f"Average score: {avg:.1f}")

    max_s: int = max([s for _, s, _, _ in data])
    top_n: str = [n for n, s, _, _ in data if s == max_s][0]

    print(f"Top performer: {top_n} ({max_s} pts, {a_counts[top_n]} "
          "achievements)")


if __name__ == "__main__":
    main()
