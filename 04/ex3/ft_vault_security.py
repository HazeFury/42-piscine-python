def main() -> None:
    """Demonstrates secure file operations using context managers."""

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    read_vault: str = "../archives/classified_data.txt"
    source_vault: str = "../archives/security_protocols.txt"
    backup_vault: str = "../archives/secured_backup.txt"

    try:
        print("Initiating secure vault access...")
        with open(read_vault, 'r', encoding='utf-8') as classified_file:
            data: str = classified_file.read()

        with open(source_vault, 'r', encoding='utf-8') as security_file:
            protocol_data: str = security_file.read()

        with open(backup_vault, 'w', encoding='utf-8') as backup:
            backup.write(protocol_data)

        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        print(data.strip())
        print("\nSECURE PRESERVATION:")
        print(protocol_data.strip())
        print("Vault automatically sealed upon completion\n")

    except FileNotFoundError as e:
        print("\nERROR: Storage vault not found.")
        print(e)
        print("==> The program has been stopped safely.")
    except Exception as e:
        print(f"CRITICAL ERROR: Extraction failed - {e}")
    else:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
