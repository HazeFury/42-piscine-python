def main() -> None:
    """Recovers ancient text from the specified storage vault."""

    vault_path: str = "../archives/ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        with open(vault_path, 'r', encoding='utf-8') as vault:
            print("Connection established...\n")

            print("RECOVERED DATA:")
            recovered_data: str = vault.read()
            print(recovered_data)

            print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found")
    except Exception as e:
        print(f"CRITICAL ERROR: Matrix collapse - {e}")


if __name__ == "__main__":
    main()
