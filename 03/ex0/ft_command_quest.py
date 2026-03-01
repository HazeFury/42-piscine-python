import sys


def main() -> None:
    """Interprets and displays command line arguments."""

    print("=== Command Quest ===")

    total_args = len(sys.argv)
    args_received = total_args - 1
    program_name = sys.argv[0]

    if args_received == 0:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")

    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {args_received}")

        index = 1
        for arg in sys.argv[1:]:
            print(f"Argument {index}: {arg}")
            index += 1

        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
