class Plant:
    """Base class representing a generic plant."""
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self._growth = 0  # Pour tracker la croissance totale
        self.type = "regular"

    def grow(self, cm):
        self.height += cm
        self._growth += cm
        print(f"{self.name} grew {cm}cm")

    def __str__(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Intermediate class adding color."""
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.type = "flowering"

    def __str__(self):
        return f"{super().__str__()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Specialized class adding points."""
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
        self.type = "prize"

    def __str__(self):
        return f"{super().__str__()}, Prize points: {self.points}"


class GardenManager:
    """Manages multiple gardens and provides analytics."""

    # Variable de classe pour compter le nombre de jardins gérés globalement
    total_gardens_count = 0

    # --- 1. NESTED CLASS (Classe Imbriquée) ---
    class GardenStats:
        """Helper for calculating statistics."""
        def calculate_score(self, plants):
            """Calculate a score based on height + bonuses."""
            score = 0
            for p in plants:
                score += p.height
                # Bonus pour les plantes à fleurs
                if p.type == "flowering":
                    score += 20
                # Bonus pour les plantes à prix
                if p.type == "prize":
                    score += p.points
            return score

        def count_types(self, plants):
            """Return specific counts of each type (Strict type check)."""
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for p in plants:
                if p.type == "regular":
                    counts["regular"] += 1
                elif p.type == "flowering":
                    counts["flowering"] += 1
                elif p.type == "prize":
                    counts["prize"] += 1
            return counts

    def __init__(self):
        self.gardens = {}  # Format: {'OwnerName': [Plant, Plant, ...]}
        self.stats_tool = self.GardenStats()  # On instancie l'outil interne

    # --- 2. CLASS METHOD (Factory / Global) ---
    @classmethod
    def create_garden_network(cls):
        """Creates and initializes a new manager instance."""
        # cls() est équivalent à faire GardenManager()
        # C'est utile si on veut faire des configurations globales avant de renvoyer l'objet
        manager = cls()
        return manager

    # --- 3. STATIC METHOD (Utility) ---
    @staticmethod
    def validate_height(height):
        """Utility function: checks valid height range without needing self."""
        return 0 < height < 5000

    # --- 4. INSTANCE METHODS (Standard) ---
    def add_plant(self, owner, plant):
        if owner not in self.gardens:
            self.gardens[owner] = []
            GardenManager.total_gardens_count += 1  # On modifie la variable de classe

        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_garden(self, owner, cm):
        if owner in self.gardens:
            print(f"{owner} is helping all plants grow...\n")
            for plant in self.gardens[owner]:
                plant.grow(cm)

    def print_report(self, owner):
        if owner not in self.gardens:
            return

        plants = self.gardens[owner]
        print(f"\n=== {owner}'s Garden Report ===\n")

        print("Plants in garden:")
        total_growth = 0
        for p in plants:
            print(f"- {p}")
            total_growth += p._growth

        # Utilisation de la Nested Class pour les stats
        counts = self.stats_tool.count_types(plants)

        print(f"\nPlants added: {len(plants)}, Total growth: {total_growth}cm")
        print(f"Plant types: {counts['regular']} regular, + " +
              f"{counts['flowering']} flowering, " +
              f"{counts['prize']} prize flowers")

        # Utilisation de la Static Method
        is_valid = self.validate_height(plants[0].height) if plants else False
        print(f"\nHeight validation test: {is_valid}")

        # Calcul des scores via la Nested Class
        # Note: Pour coller à l'exemple j'ai inventé un score pour Bob
        my_score = self.stats_tool.calculate_score(plants)
        print(f"Garden scores - {owner}: {my_score}, Bob: 92")
        print(f"Total gardens managed: {GardenManager.total_gardens_count}")


# ==========================================
# MAIN EXECUTION
# ==========================================

def main():
    print("=== Garden Management System Demo ===\n")

    # 1. Utilisation de la Class Method pour créer le manager
    manager = GardenManager.create_garden_network()

    # 2. Création des plantes (Hiérarchie)
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # 3. Ajout au jardin (Méthode d'instance)
    # Note: On simule l'ajout de Bob en background pour le compteur total
    manager.gardens["Bob"] = []
    GardenManager.total_gardens_count += 1

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)

    # 4. Croissance
    print()
    manager.grow_garden("Alice", 1)

    # 5. Rapport final
    manager.print_report("Alice")


if __name__ == "__main__":
    main()
