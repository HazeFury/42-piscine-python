import sys


try:
    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    import requests  # type: ignore

    DEPENDENCIES_LOADED: bool = True
except ImportError:
    DEPENDENCIES_LOADED = False


def check_env() -> None:
    """Check"""
    python_path: str = sys.executable

    print("\nChecking env:")
    print(f"Executing from: {python_path}")

    if "pypoetry" in python_path or "poetry" in python_path.lower():
        print("[INFO] Managed by: Poetry (Centralized Cache Environment)")
    elif ".venv" in python_path:
        print("[INFO] Managed by: pip (Local Virtual Environment)")
    else:
        print("[WARNING] Managed by: Global System")


def check_dependencies() -> None:
    """Vérifie l'état des dépendances et affiche un rapport."""
    print("\nLOADING STATUS: Loading programs...\n")
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
    """Simule une analyse basique pour démontrer l'usage des dépendances."""
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    # 1. NUMPY : créer une liste de chiffres de 0 à 999.
    # np.arange(1000) génère [0, 1, 2, ..., 999]
    donnees_brutes: np.ndarray = np.arange(1000)

    # 2. PANDAS : créer "tableau Excel" (DataFrame) avec une seule colonne
    # qu'on appelle "Signal".
    df: pd.DataFrame = pd.DataFrame(donnees_brutes, columns=["Signal"])

    print("Generating visualization...")

    # 3. MATPLOTLIB : dessiner les valeurs de la colonne "Signal"
    plt.plot(df["Signal"], color="green")

    # Sauvegarde du graphique
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Fonction principale d'orchestration."""
    try:
        check_dependencies()
        check_env()
        analyze_matrix_data()
    except Exception as e:
        print(f"An unexpected anomaly occurred in the Matrix: {e}")


if __name__ == "__main__":
    main()
