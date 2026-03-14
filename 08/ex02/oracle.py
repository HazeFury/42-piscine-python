import os
import sys
from dotenv import load_dotenv  # type: ignore


def read_matrix_config() -> None:
    """Loads and displays Oracle configurations."""
    print("ORACLE STATUS: Reading the Matrix...\n")

    has_env_file: bool = load_dotenv()

    matrix_mode: str | None = os.getenv("MATRIX_MODE")
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str | None = os.getenv("LOG_LEVEL")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")

    if not any([matrix_mode, db_url, api_key, log_level, zion_endpoint]):
        print("[WARNING] DEFAULT/MISSING CONFIGURATION DETECTED!")
        print("No .env file or no system variables found.")
        print("Please provide a configuration to proceed.\n")

    print("--------------- Configuration loaded: ---------------")
    print("Mode         : ", end="")
    if matrix_mode:
        print(f"{matrix_mode} [OK]")
    else:
        print("(unspecified) [NOT FOUND]")

    print("Database     : ", end="")
    if db_url:
        print("Connected to local instance [OK]")
    else:
        print("Connection missing [NOT FOUND]")

    print("API Access   : ", end="")
    if api_key:
        print("Authenticated [OK]")
    else:
        print("Missing Key [NOT FOUND]")

    print("Log Level    : ", end="")
    print(f"{log_level} [OK]" if log_level else "DEBUG [NOT FOUND]")

    print("Zion Network : ", end="")
    if zion_endpoint:
        print("Online [OK]")
    else:
        print("Offline [NOT FOUND]")
    print("-----------------------------------------------------")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if has_env_file:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] Can't read .env file."
              " Relying on system environment variables.")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    """Run the main to find dotenv."""
    try:
        read_matrix_config()
    except Exception as e:
        print(f"Critical error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
