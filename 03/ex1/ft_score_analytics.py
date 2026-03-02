import sys


def main() -> None:
    """Processes command-line scores and displays analytics."""

    print("=== Player Score Analytics ===")

    args = sys.argv[1:]
    if len(args) == 0:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []

    try:
        for arg in args:
            scores.append(int(arg))
    except ValueError:
        print(f"Error: '{arg}' is not a valid numeric score!")
        return

    total_players: int = len(scores)
    total_score: int = sum(scores)
    average: float = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
