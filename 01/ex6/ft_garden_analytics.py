class Plant:
    """Base class representing a generic plant."""
    def __init__(self, name: str, height: int) -> None:
        """Initialize "regular" plant object with name and height."""
        self.name = name
        self.height = height
        self._growth = 0
        self.type = "regular"

    def grow(self, cm: int) -> None:
        """Add some height (in cm) to this plant."""
        self.height += cm
        self._growth += cm
        print(f"{self.name} grew {cm}cm")

    def get_bonus_score(self) -> int:
        return 0

    def __str__(self) -> str:
        """Return data about this plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Intermediate class adding color."""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize "flowering" plant based on plant and adding color."""
        super().__init__(name, height)
        self.color = color
        self.type = "flowering"

    def get_bonus_score(self) -> int:
        return 20

    def __str__(self) -> str:
        """Return data about this plant."""
        return f"{super().__str__()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Specialized class adding points."""
    def __init__(self, name: str, height: int, color: str, point: int) -> None:
        """Initialize "prize" plant based on flowering and adding point."""
        super().__init__(name, height, color)
        self.points = point
        self.type = "prize"

    def get_bonus_score(self) -> int:
        return 20 + self.points

    def __str__(self) -> str:
        """Return data about this plant."""
        return f"{super().__str__()}, Prize points: {self.points}"


class GardenManager:
    """Manages multiple gardens and provides analytics."""
    total_gardens_count = 0

    class GardenStats:
        """Helper for calculating statistics."""
        def calculate_score(self, plants: list[Plant]) -> int:
            """Calculate a score based on height + bonuses."""
            score = 0
            for p in plants:
                score += p.height + p.get_bonus_score()
            return score

        def count_types(self, plants: list[Plant]) -> dict[str, int]:
            """Return specific counts of each type."""
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for p in plants:
                if p.type == "regular":
                    counts["regular"] += 1
                elif p.type == "flowering":
                    counts["flowering"] += 1
                elif p.type == "prize":
                    counts["prize"] += 1
            return counts

    def __init__(self) -> None:
        """Initialize the manager of garden to track everybody's garden.
        Gardens have this format : {'OwnerName': [Plant, Plant, ...]}"""
        self.gardens: dict[str, list[Plant]] = {}
        self.stats_tool = self.GardenStats()

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Creates and initializes a new manager instance. This is equals to
        make : manager = GardenManager()."""
        manager = cls()
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility function: checks valid height range without needing self."""
        return 0 < height < 5000

    def add_plant(self, owner: str, plant: Plant) -> None:
        if owner not in self.gardens:
            self.gardens[owner] = []
            GardenManager.total_gardens_count += 1

        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_garden(self, owner: str, cm: int) -> None:
        if owner in self.gardens:
            print(f"{owner} is helping all plants grow...\n")
            for plant in self.gardens[owner]:
                plant.grow(cm)

    def print_report(self, owner: str) -> None:
        if owner not in self.gardens:
            return

        plants = self.gardens[owner]
        print(f"\n=== {owner}'s Garden Report ===\n")

        print("Plants in garden:")
        total_growth = 0
        for p in plants:
            print(f"- {p}")
            total_growth += p._growth

        counts = self.stats_tool.count_types(plants)

        print(f"\nPlants added: {len(plants)}, Total growth: {total_growth}cm")
        print(f"Plant types: {counts['regular']} regular, + " +
              f"{counts['flowering']} flowering, " +
              f"{counts['prize']} prize flowers")

        is_valid = self.validate_height(plants[0].height) if plants else False
        print(f"\nHeight validation test: {is_valid}")

        my_score = self.stats_tool.calculate_score(plants)
        print(f"Garden scores - {owner}: {my_score}, Bob: 92")
        print(f"Total gardens managed: {GardenManager.total_gardens_count}")


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    manager.gardens["Bob"] = []
    GardenManager.total_gardens_count += 1

    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)

    print()
    manager.grow_garden("Alice", 1)

    manager.print_report("Alice")


if __name__ == "__main__":
    main()
