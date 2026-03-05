def crisis_handler(filename: str, is_routine: bool = False) -> None:
    """Attempts to read an archive and handles potential system crises."""

    base_dir: str = "../archives/"
    filepath: str = base_dir + filename

    if is_routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filepath, 'r', encoding='utf-8') as vault:
            content: str = vault.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"RESPONSE: Unknown anomaly detected - {e}")
        print("STATUS: Crisis contained, investigating\n")


def main() -> None:
    """Runs the Crisis Response System simulation."""

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")

    crisis_handler("classified_vault.txt")

    crisis_handler("standard_archive.txt", is_routine=True)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
