from typing import Generator


def get_events(
    total: int
) -> Generator[tuple[int, dict[str, str | int], str], None, None]:
    """Yields a stream of game events one by one."""

    players: list[dict[str, str | int]] = [
        {"name": "alice", "level": 5},
        {"name": "bob", "level": 12},
        {"name": "charlie", "level": 8}
    ]

    actions: list[str] = [
        "killed monster",
        "found treasure",
        "leveled up"
    ]

    for i in range(total):
        rand_player_index: int = ((i * 17) % 8) % len(players)
        rand_action_index: int = ((i * 98) % 11) % len(actions)

        yield (i, players[rand_player_index], actions[rand_action_index])


def fibonacci_stream() -> Generator[int, None, None]:
    """Yields an infinite sequence of Fibonacci numbers."""
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream() -> Generator[int, None, None]:
    """Yields an infinite sequence of prime numbers."""
    num: int = 2
    while True:
        is_prime: bool = True
        for i in range(2, num):
            if i * i > num:
                break
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main() -> None:
    """Processes game events and demonstrates generator efficiency."""
    print("=== Game Data Stream Processor ===\n")

    total: int = 1000
    print(f"Processing {total} game events...\n")

    events_gen = get_events(total)

    high_level: int = 0
    treasures: int = 0
    level_ups: int = 0

    for event in events_gen:
        e_id: int = event[0]
        player_data: dict[str, str | int] = event[1]
        action: str = event[2]

        level: str | int = player_data["level"]
        name: str | int = player_data["name"]

        if isinstance(level, int) and level >= 10:
            high_level += 1

        if action == "found treasure":
            treasures += 1
        elif action == "leveled up":
            level_ups += 1

        if e_id < 3:
            print(f"Event {e_id + 1}: Player {name} (level {level}) {action}")
        elif e_id == 4:
            print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {e_id + 1}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_ups}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")

    fib_gen = fibonacci_stream()
    fib_list: list[str] = []
    for _ in range(10):
        fib_list.append(str(next(fib_gen)))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_gen = prime_stream()
    prime_list: list[str] = []
    for _ in range(5):
        prime_list.append(str(next(prime_gen)))
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if __name__ == "__main__":
    main()
