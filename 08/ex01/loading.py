import sys


try:
    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    import matplotlib  # type: ignore
    import requests  # type: ignore

    DEPENDENCIES_LOADED = True
except ImportError:
    DEPENDENCIES_LOADED = False


def check_env() -> None:
    python_path = sys.executable

    print("Checking env:")
    print(f"Executing from: {python_path}")

    if "pypoetry" in python_path or "poetry" in python_path.lower():
        print("[INFO] Managed by: Poetry (Centralized Cache Environment)")
    elif ".venv" in python_path:
        print("[INFO] Managed by: pip (Local Virtual Environment)")
    else:
        print("[WARNING] Managed by: Global System")


def check_dependencies() -> None:
    """Vérifie l'état des dépendances et affiche un rapport."""
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    if not DEPENDENCIES_LOADED:
        print("\nCRITICAL ERROR: Matrix dependencies are missing!")
        print("Please install them using pip or Poetry:")
        print("  pip install -r requirements.txt")
        print("  OR")
        print("  poetry install")
        sys.exit(1)

    print(f"[OK] pandas ({pd.__version__}) Data manipulation ready")
    print(f"[OK] requests ({requests.__version__}) Network access ready")
    print(f"[OK] matplotlib ({matplotlib.__version__}) Visualization ready")


def analyze_matrix_data() -> None:
    """Simule une analyse de données et génère un graphique."""
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    # Création de 1000 points de données aléatoires avec numpy
    data = np.random.randn(1000)
    # Transformation en tableau (DataFrame) avec pandas
    df = pd.DataFrame(data, columns=["Matrix Signals"])

    print("Generating visualization...")
    # Création d'un graphique avec matplotlib
    plt.figure(figsize=(10, 6))
    # On fait une somme cumulée (cumsum) pour avoir une jolie courbe qui
    # monte/descend
    plt.plot(
        df["Matrix Signals"].cumsum(), color="green", label="Signal Strength"
        )
    plt.title("Matrix Network Signal Analysis")
    plt.legend()

    # Sauvegarde du fichier comme exigé par l'output
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Fonction principale d'orchestration."""
    try:
        check_dependencies()
        check_env()
        if DEPENDENCIES_LOADED:
            analyze_matrix_data()
    except Exception as e:
        print(f"An unexpected anomaly occurred in the Matrix: {e}")


if __name__ == "__main__":
    main()
