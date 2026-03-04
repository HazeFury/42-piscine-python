def main() -> None:
    """Creates a new archive entry with critical quantum data."""

    vault_name: str = "new_discovery.txt"
    vault_path: str = f"../archives/{vault_name}"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {vault_name}")

    entries: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by marberge"
    ]

    try:
        with open(vault_path, 'w', encoding='utf-8') as vault:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")

            for entry in entries:
                print(entry)
                vault.write(entry + "\n")

            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{vault_name}' ready for long-term preservation.")

    except FileNotFoundError:
        print("ERROR: Storage sector './archives/' is missing.")
    except PermissionError:
        print("ERROR: Archival clearance denied. Check permissions.")
    except Exception as e:
        print(f"CRITICAL ERROR: Matrix collapse - {e}")


if __name__ == "__main__":
    main()
