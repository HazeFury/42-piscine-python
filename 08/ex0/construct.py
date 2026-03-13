import sys
import os
import site


def is_in_virtual_env() -> bool:
    """
    Detects if the script is running inside a virtual environment.
    Compares the current prefix with the base installation prefix.
    """
    try:
        return sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    except Exception as e:
        print(f"Error checking environment: {e}")
        return False


def get_venv_name() -> str | None:
    """
    Extracts the name of the active virtual environment.
    """
    try:
        venv_path = os.environ.get("VIRTUAL_ENV")
        if venv_path:
            return os.path.basename(venv_path)

        if is_in_virtual_env():
            return os.path.basename(sys.prefix)
        return None
    except Exception as e:
        print(f"Error getting venv name: {e}")
        return None


def main() -> None:
    """Main execution function handling both environment states."""
    try:
        current_python = sys.executable

        if is_in_virtual_env():
            # --- INSIDE THE MATRIX (VENV) ---
            venv_name = get_venv_name()
            env_path = sys.prefix

            pkg_paths = site.getsitepackages()
            pkg_path = pkg_paths[0] if pkg_paths else "Unknown path"

            print("MATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {current_python}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {env_path}\n")
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting"
                  "the global system.\n")
            print("Package installation path:")
            print(pkg_path)

        else:
            # --- OUTSIDE THE MATRIX (GLOBAL ENV) ---
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {current_python}")
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows\n")
            print("Then run this program again.")

    except Exception as e:
        print(f"Critical system failure: {e}")


if __name__ == "__main__":
    main()
